FROM python:3.12-slim

WORKDIR /srv

COPY app/backend/requirements.txt /srv/requirements.txt
RUN pip install --no-cache-dir -r /srv/requirements.txt

COPY app/ /srv/app/

ENV DB_PATH=/srv/data/test.db
VOLUME ["/srv/data"]
EXPOSE 8000

WORKDIR /srv/app/backend
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
