# syntax=docker/dockerfile:1.7-labs

FROM python:3.11 as requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export \
    -f requirements.txt \
    --output requirements.txt \
    --without-hashes \
    --without dev

FROM python:3.11-slim

WORKDIR /app

COPY --from=requirements-stage /tmp/requirements.txt /app/requirements.txt

RUN pip install \
    -r /app/requirements.txt \
    --no-cache-dir \
    --upgrade

COPY --parents ./src/ ./application.toml /app/

ENV PYTHONPATH=/app/src


CMD ["fastapi", "run", "/app/src/main.py", "--port", "80"]
