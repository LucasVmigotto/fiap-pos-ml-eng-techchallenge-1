# syntax=docker/dockerfile:1

FROM python:3.11

ENV API_HOST='0.0.0.0'
ENV API_HOST=80

COPY ../../requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY ../../src /app/src

CMD [\
    "python", "-m", "uvicorn", "src.main:app", \
    "--host", "${API_HOST}", \
    "--port", "${API_PORT}"\
    ]
