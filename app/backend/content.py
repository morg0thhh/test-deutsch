"""Содержание теста.

Правильные ответы живут ТОЛЬКО здесь, на сервере: клиенту отдаётся
версия без ключей (см. public_questions()), чтобы нельзя было подсмотреть
ответы в исходнике страницы.

Видео для аудирования проверены 2026-09-30: все три существуют и
разрешены к встраиванию (playableInEmbed=true). Вопросы составлены
по реальным субтитрам, тайм-коды указывают на нужный фрагмент.
"""

SECTIONS = [
    {"id": "hoeren", "title": "Hören", "subtitle": "Аудирование", "icon": "🎧"},
    {"id": "lesen", "title": "Lesen", "subtitle": "Чтение", "icon": "📖"},
    {"id": "grammatik", "title": "Grammatik & Wortschatz", "subtitle": "Грамматика и лексика", "icon": "🧩"},
    {"id": "schreiben", "title": "Schreiben", "subtitle": "Письмо", "icon": "✍️"},
]

# Видео: id -> метаданные (для подписи и ссылки «открыть на YouTube»)
VIDEOS = {
    "eROGKw-gnsA": {"title": "Start Deutsch 1 Hören — A1 Listening Exercises", "author": "Grenzenlosci"},
    "5smhFjhCSY0": {"title": "A2 Hören Übungen — Goethe & TELC", "author": "Wordifi"},
    "VBg_F6NERzI": {"title": "Goethe / ÖSD Zertifikat B1 — Modul Hören, Teil 1", "author": "DEUTSCH-INSTITUT"},
}

QUESTIONS = [
    # ---------------- HÖREN ----------------
    {
        "id": "h1", "section": "hoeren", "level": "A1", "type": "choice",
        "video": {"id": "eROGKw-gnsA", "start": 70, "hint": "Aufgabe 1 — im Geschäft"},
        "prompt": "Was kostet der Mantel heute?",
        "options": ["65,00 €", "60,50 €", "50,00 €"],
        "answer": 1,
    },
    {
        "id": "h2", "section": "hoeren", "level": "A1", "type": "choice",
        "video": {"id": "eROGKw-gnsA", "start": 274, "hint": "Aufgabe 4 — Telefongespräch"},
        "prompt": "Wann gehen Anja und ihre Freundin ins Kino?",
        "options": ["Am Freitag", "Am Samstag", "Am Sonntag"],
        "answer": 2,
    },
    {
        "id": "h3", "section": "hoeren", "level": "A2", "type": "choice",
        "video": {"id": "5smhFjhCSY0", "start": 44, "hint": "Gespräch: Julia und Thomas"},
        "prompt": "Wie viele Freunde haben bisher zugesagt?",
        "options": ["Vier", "Sechs", "Zehn"],
        "answer": 1,
    },
    {
        "id": "h4", "section": "hoeren", "level": "A2", "type": "choice",
        "video": {"id": "5smhFjhCSY0", "start": 44, "hint": "dasselbe Gespräch"},
        "prompt": "Was bringt Thomas zum Essen mit?",
        "options": ["Pizza", "Getränke", "Einen Nudelsalat"],
        "answer": 2,
    },
    {
        "id": "h5", "section": "hoeren", "level": "B1", "type": "choice",
        "video": {"id": "VBg_F6NERzI", "start": 193, "hint": "Durchsage am Flughafen"},
        "prompt": "Wo müssen die Passagiere nach München einchecken?",
        "options": ["Am Schalter 53", "Am Schalter 45", "Am Schalter 39"],
        "answer": 1,
    },
    {
        "id": "h6", "section": "hoeren", "level": "B1", "type": "choice",
        "video": {"id": "VBg_F6NERzI", "start": 305, "hint": "Meldung im Radio"},
        "prompt": "Wie oft gehen Deutsche im Durchschnitt zum Arzt?",
        "options": ["Einmal im Monat", "Alle sechs Wochen", "Alle zwei Monate"],
        "answer": 2,
    },

    # ---------------- LESEN ----------------
    {
        "id": "l1", "section": "lesen", "level": "A1", "type": "choice",
        "text": "Liebe Nachbarn,\n\nam Samstag, dem 12. April, putzen wir gemeinsam den Hof. "
                "Wir treffen uns um 10 Uhr vor dem Haus Nr. 7. Bitte bringen Sie Handschuhe mit. "
                "Getränke gibt es umsonst!",
        "prompt": "Was sollen die Nachbarn mitbringen?",
        "options": ["Getränke", "Handschuhe", "Einen Besen"],
        "answer": 1,
    },
    {
        "id": "l2", "section": "lesen", "level": "A2", "type": "choice",
        "text": "Hallo Nina,\n\nleider muss ich unseren Termin am Mittwoch verschieben. Mein Chef hat mich "
                "für eine Fortbildung angemeldet, die den ganzen Tag dauert. Hättest du am Donnerstag "
                "um 17 Uhr Zeit? Wenn nicht, geht es auch nächste Woche. Sag mir einfach Bescheid.\n\n"
                "Liebe Grüße\nTom",
        "prompt": "Warum schreibt Tom?",
        "options": [
            "Er möchte den Termin verschieben.",
            "Er lädt Nina zu einer Fortbildung ein.",
            "Er sagt den Termin endgültig ab.",
        ],
        "answer": 0,
    },
    {
        "id": "l3", "section": "lesen", "level": "B1", "type": "choice",
        "text": "Immer mehr Städte in Deutschland richten autofreie Zonen ein. Befürworter argumentieren, "
                "dass die Luft dadurch sauberer wird und Kinder sicherer spielen können. Einzelhändler "
                "dagegen befürchten, dass ihnen Kunden wegbleiben, wenn diese nicht mehr direkt vor dem "
                "Geschäft parken können. Untersuchungen aus Kopenhagen zeigen allerdings, dass die Umsätze "
                "in Fußgängerzonen langfristig eher steigen.",
        "prompt": "Was zeigen die Untersuchungen aus Kopenhagen?",
        "options": [
            "Die Umsätze in Fußgängerzonen steigen langfristig eher.",
            "Die Einzelhändler verlieren ihre Kunden.",
            "Autofreie Zonen sind für Kinder gefährlich.",
        ],
        "answer": 0,
    },
    {
        "id": "l4", "section": "lesen", "level": "B2", "type": "choice",
        "text": "Dass Homeoffice die Produktivität steigere, gilt vielen inzwischen als ausgemacht. Die "
                "Datenlage ist jedoch weniger eindeutig, als die Debatte vermuten lässt: Während Beschäftigte "
                "mit klar abgegrenzten Einzelaufgaben tatsächlich effizienter arbeiten, büßen Teams, deren "
                "Arbeit auf spontaner Abstimmung beruht, messbar an Tempo ein. Pauschale Empfehlungen führen "
                "daher in die Irre.",
        "prompt": "Welche Aussage entspricht dem Text?",
        "options": [
            "Homeoffice steigert die Produktivität in jedem Fall.",
            "Der Effekt hängt davon ab, wie die Arbeit organisiert ist.",
            "Teams arbeiten im Homeoffice grundsätzlich schneller.",
        ],
        "answer": 1,
    },

    # ---------------- GRAMMATIK & WORTSCHATZ ----------------
    {
        "id": "g1", "section": "grammatik", "level": "A1", "type": "choice",
        "prompt": "Ich ___ aus Russland.",
        "options": ["komme", "kommst", "kommt"], "answer": 0,
    },
    {
        "id": "g2", "section": "grammatik", "level": "A1", "type": "choice",
        "prompt": "___ Tisch ist neu.",
        "options": ["Der", "Die", "Das"], "answer": 0,
    },
    {
        "id": "g3", "section": "grammatik", "level": "A1", "type": "choice",
        "prompt": "Am Wochenende fahren wir ___ Berlin.",
        "options": ["zu", "nach", "in"], "answer": 1,
    },
    {
        "id": "g4", "section": "grammatik", "level": "A2", "type": "choice",
        "prompt": "Gestern ___ ich ins Kino gegangen.",
        "options": ["habe", "bin", "war"], "answer": 1,
    },
    {
        "id": "g5", "section": "grammatik", "level": "A2", "type": "choice",
        "prompt": "Ich helfe ___ Freund.",
        "options": ["meinen", "meinem", "meines"], "answer": 1,
    },
    {
        "id": "g6", "section": "grammatik", "level": "B1", "type": "choice",
        "prompt": "Wenn ich mehr Zeit hätte, ___ ich öfter Sport machen.",
        "options": ["werde", "würde", "wäre"], "answer": 1,
    },
    {
        "id": "g7", "section": "grammatik", "level": "B1", "type": "choice",
        "prompt": "Das Fahrrad, ___ ich gekauft habe, war ziemlich teuer.",
        "options": ["den", "das", "dem"], "answer": 1,
    },
    {
        "id": "g8", "section": "grammatik", "level": "B2", "type": "choice",
        "prompt": "___ des schlechten Wetters fand das Fest im Freien statt.",
        "options": ["Wegen", "Trotz", "Während"], "answer": 1,
    },
    {
        "id": "g9", "section": "grammatik", "level": "B2", "type": "choice",
        "prompt": "Der Antrag muss bis Freitag ___ werden.",
        "options": ["einreichen", "einzureichen", "eingereicht"], "answer": 2,
    },

    # ---------------- SCHREIBEN (не оценивается автоматически) ----------------
    {
        "id": "s1", "section": "schreiben", "level": "A2", "type": "text",
        "prompt": "Schreiben Sie eine kurze Nachricht an eine Freundin: Sie können heute Abend nicht kommen. "
                  "Erklären Sie warum und schlagen Sie einen neuen Termin vor. (ca. 30–40 Wörter)",
        "placeholder": "Liebe …",
    },
    {
        "id": "s2", "section": "schreiben", "level": "A1", "type": "text",
        "prompt": "Was machen Sie gern in Ihrer Freizeit? Schreiben Sie 3–5 Sätze.",
        "placeholder": "In meiner Freizeit …",
    },
]

LEVELS = ["A1", "A2", "B1", "B2"]
LEVEL_LABELS = {
    "A0": ("A0 — самое начало", "Начинаем с алфавита и первых фраз. Это нормальный старт, всё впереди."),
    "A1": ("A1 — базовый", "Простые фразы о себе и быте уже даются. Дальше — прошедшее время и больше лексики."),
    "A2": ("A2 — элементарный", "Хорошая база: быт, планы, короткие письма. Пора выходить в связную речь."),
    "B1": ("B1 — пороговый", "Уверенно держите бытовые темы и понимаете объявления. Дальше — аргументация."),
    "B2": ("B2 — продвинутый", "Понимаете сложные тексты и абстрактные темы. Работаем над точностью и стилем."),
}

# Сколько котиков закрашивать на шкале (из 5)
LEVEL_CATS = {"A0": 1, "A1": 2, "A2": 3, "B1": 4, "B2": 5}

AUTO_QUESTIONS = [q for q in QUESTIONS if q["type"] == "choice"]
TOTAL_AUTO = len(AUTO_QUESTIONS)


def public_questions():
    """Вопросы без ключей — то, что уходит в браузер."""
    out = []
    for i, q in enumerate(QUESTIONS):
        pq = {
            "id": q["id"], "section": q["section"], "type": q["type"],
            "prompt": q["prompt"], "index": i,
        }
        if "options" in q:
            pq["options"] = q["options"]
        if "text" in q:
            pq["text"] = q["text"]
        if "placeholder" in q:
            pq["placeholder"] = q["placeholder"]
        if "video" in q:
            v = dict(q["video"])
            v.update(VIDEOS.get(v["id"], {}))
            pq["video"] = v
        out.append(pq)
    return out


def evaluate(answers: dict):
    """answers: {question_id: индекс варианта или текст}.

    Уровень = самый высокий L, на котором и на всех уровнях ниже
    набрано >= 60% правильных. Так одна случайная удача на B2 не
    поднимает результат, а провал на A1 не даёт проскочить дальше.
    """
    per_level = {lv: {"correct": 0, "total": 0} for lv in LEVELS}
    per_section = {}
    details = []

    for q in AUTO_QUESTIONS:
        given = answers.get(q["id"])
        ok = isinstance(given, int) and given == q["answer"]
        lv = q["level"]
        per_level[lv]["total"] += 1
        per_level[lv]["correct"] += int(ok)

        s = per_section.setdefault(q["section"], {"correct": 0, "total": 0})
        s["total"] += 1
        s["correct"] += int(ok)

        details.append({
            "id": q["id"], "section": q["section"], "level": lv,
            "correct": ok, "given": given, "expected": q["answer"],
        })

    level = "A0"
    for lv in LEVELS:
        st = per_level[lv]
        if st["total"] and st["correct"] / st["total"] >= 0.6:
            level = lv
        else:
            break

    written = {q["id"]: answers.get(q["id"], "") for q in QUESTIONS if q["type"] == "text"}
    total_correct = sum(1 for d in details if d["correct"])

    title, comment = LEVEL_LABELS[level]
    return {
        "level": level,
        "level_title": title,
        "level_comment": comment,
        "cats": LEVEL_CATS[level],
        "correct": total_correct,
        "total": TOTAL_AUTO,
        "per_level": per_level,
        "per_section": per_section,
        "details": details,
        "written": written,
    }
