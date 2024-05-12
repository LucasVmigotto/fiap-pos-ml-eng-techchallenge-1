# syntax=docker/dockerfile:1

FROM mcr.microsoft.com/devcontainers/python:3.11

ARG USERNAME='vscode'

USER ${USERNAME}

WORKDIR /app

RUN pipx install poetry

RUN pipx inject poetry poetry-plugin-export

COPY ./pyproject.toml ./poetry.lock* /app/

RUN poetry install --with dev

ENV PYTHONPATH=/app/src
