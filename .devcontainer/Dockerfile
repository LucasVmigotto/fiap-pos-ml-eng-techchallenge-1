# syntax=docker/dockerfile:1

FROM mcr.microsoft.com/devcontainers/python:3.11

# [Optional] - Create a non-root user (vscode already has UID 1000)
# ARG USERNAME='jovyan'
# ARG USER_UID=1001
# ARG USER_GID=${USER_UID}
#
# RUN groupadd --gid ${USER_GID} ${USERNAME} \
#     && useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME} \
#     && apt-get update \
#     && apt-get install -y sudo \
#     && echo ${USERNAME} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/${USERNAME} \
#     && chmod 0440 /etc/sudoers.d/${USERNAME}

WORKDIR /app

RUN pipx install poetry

RUN pipx inject poetry poetry-plugin-export

COPY ./pyproject.toml ./poetry.lock* /app/

RUN ls -la

RUN poetry export -f requirements.txt --with dev --output /tmp/requirements.txt --without-hashes

RUN pip3 \
    --disable-pip-version-check \
    --no-cache-dir install \
    -r /tmp/requirements.txt \
    && \
    rm -rf /tmp/requirements.txt

ENV PYTHONPATH=/app/src
