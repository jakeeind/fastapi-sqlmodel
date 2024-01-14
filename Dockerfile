FROM python:3.11-bookworm
RUN apt update --fix-missing
RUN apt install -y python3 python3-dev python3-pip python3-venv npm git locales

# install postgresql
RUN apt install -y libpq-dev

RUN sed -i '/th_TH.UTF-8/s/^# //g' /etc/locale.gen && locale-gen
ENV LANG th_TH.UTF-8
ENV LANGUAGE th_TH:en

WORKDIR /app
COPY pyproject.toml /app
COPY poetry.lock /app

RUN python3 -m venv /venv
ENV PYTHON=/venv/bin/python3
RUN $PYTHON -m pip install wheel poetry uvicorn
RUN $PYTHON -m pip install wheel poetry gunicorn

RUN $PYTHON -m poetry config virtualenvs.create false && $PYTHON -m poetry install --no-interaction --only main

COPY . /app/
