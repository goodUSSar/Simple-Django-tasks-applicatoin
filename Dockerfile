# syntax=docker/dockerfile:1

FROM python:3.14-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_NO_CACHE_DIR=1

RUN groupadd --system app \
    && useradd --system \
        --gid app \
        --home-dir /app \
        --create-home \
        app

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install \
    --no-cache-dir \
    -r requirements.txt

COPY --chown=app:app . .

RUN mkdir -p /app/data \
    && chown -R app:app /app/data

USER app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
