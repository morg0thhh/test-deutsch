"""Einstufungstest — бэкенд.

Держит содержание теста, ключи к ответам, профили и рейтинг.
Хранилище — SQLite, один файл, никаких внешних сервисов.
"""
import json
import os
import secrets
import sqlite3
import time
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

import content

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "static"
DB_PATH = Path(os.environ.get("DB_PATH", BASE_DIR / "data" / "test.db"))
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

CAT_FILES = sorted(p.name for p in (STATIC_DIR / "cats").iterdir() if p.suffix in {".jpg", ".png"})

app = FastAPI(title="Deutsch Einstufungstest")


def db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with db() as conn:
        conn.executescript("""
        CREATE TABLE IF NOT EXISTS players (
            id          TEXT PRIMARY KEY,
            token       TEXT NOT NULL,
            name        TEXT NOT NULL,
            avatar      TEXT NOT NULL,
            created_at  REAL NOT NULL,
            updated_at  REAL NOT NULL,
            step        INTEGER NOT NULL DEFAULT 0,
            section     TEXT,
            finished    INTEGER NOT NULL DEFAULT 0,
            level       TEXT,
            score       INTEGER,
            total       INTEGER,
            answers     TEXT,
            result      TEXT
        );
        """)


init_db()


# ---------------------------------------------------------------- модели

class ProfileIn(BaseModel):
    name: str = Field(min_length=1, max_length=40)
    avatar: str = Field(min_length=1, max_length=64)


class ProgressIn(BaseModel):
    id: str
    token: str
    step: int = 0
    section: str | None = None
    answers: dict = {}


class SubmitIn(BaseModel):
    id: str
    token: str
    answers: dict = {}


def auth(player_id: str, token: str):
    with db() as conn:
        row = conn.execute("SELECT * FROM players WHERE id = ?", (player_id,)).fetchone()
    if row is None or not secrets.compare_digest(row["token"], token):
        raise HTTPException(status_code=403, detail="Unbekanntes Profil")
    return row


# ---------------------------------------------------------------- API

@app.get("/api/config")
def get_config():
    return {
        "sections": content.SECTIONS,
        "questions": content.public_questions(),
        "cats": CAT_FILES,
        "total_auto": content.TOTAL_AUTO,
    }


@app.post("/api/profile")
def create_profile(p: ProfileIn):
    if p.avatar not in CAT_FILES:
        raise HTTPException(status_code=400, detail="Unbekannter Avatar")
    pid, token, now = secrets.token_urlsafe(9), secrets.token_urlsafe(24), time.time()
    with db() as conn:
        conn.execute(
            "INSERT INTO players (id, token, name, avatar, created_at, updated_at) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (pid, token, p.name.strip(), p.avatar, now, now),
        )
    return {"id": pid, "token": token, "name": p.name.strip(), "avatar": p.avatar}


@app.post("/api/progress")
def save_progress(p: ProgressIn):
    auth(p.id, p.token)
    with db() as conn:
        conn.execute(
            "UPDATE players SET step = ?, section = ?, answers = ?, updated_at = ? "
            "WHERE id = ? AND finished = 0",
            (p.step, p.section, json.dumps(p.answers, ensure_ascii=False), time.time(), p.id),
        )
    return {"ok": True}


@app.post("/api/submit")
def submit(p: SubmitIn):
    auth(p.id, p.token)
    result = content.evaluate(p.answers)
    with db() as conn:
        conn.execute(
            "UPDATE players SET finished = 1, level = ?, score = ?, total = ?, "
            "answers = ?, result = ?, updated_at = ?, step = ? WHERE id = ?",
            (result["level"], result["correct"], result["total"],
             json.dumps(p.answers, ensure_ascii=False),
             json.dumps(result, ensure_ascii=False),
             time.time(), len(content.QUESTIONS), p.id),
        )
    return result


@app.get("/api/players")
def players():
    """Рейтинг для главной: кто на каком этапе."""
    with db() as conn:
        rows = conn.execute(
            "SELECT id, name, avatar, step, section, finished, level, score, total, updated_at "
            "FROM players "
            "ORDER BY finished DESC, COALESCE(score, -1) DESC, step DESC, updated_at DESC"
        ).fetchall()
    total_q = len(content.QUESTIONS)
    return [{
        "id": r["id"], "name": r["name"], "avatar": r["avatar"],
        "step": r["step"], "section": r["section"], "finished": bool(r["finished"]),
        "level": r["level"], "score": r["score"], "total": r["total"],
        "progress": round(100 * r["step"] / total_q) if total_q else 0,
        "updated_at": r["updated_at"],
    } for r in rows]


@app.get("/api/result/{player_id}")
def get_result(player_id: str):
    """Разбор для преподавателя: что ответила, включая письменную часть."""
    with db() as conn:
        row = conn.execute("SELECT * FROM players WHERE id = ?", (player_id,)).fetchone()
    if row is None or not row["finished"]:
        raise HTTPException(status_code=404, detail="Noch kein Ergebnis")
    return {
        "name": row["name"], "avatar": row["avatar"],
        "result": json.loads(row["result"]),
        "questions": content.public_questions(),
    }


# ---------------------------------------------------------------- страницы

@app.get("/")
def index():
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/test")
def test_page():
    return FileResponse(STATIC_DIR / "test.html")


@app.get("/lehrer/{player_id}")
def teacher_page(player_id: str):
    return FileResponse(STATIC_DIR / "teacher.html")


app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
