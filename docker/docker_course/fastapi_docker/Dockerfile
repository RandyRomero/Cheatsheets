FROM python:3.11.2-alpine3.17

WORKDIR /src

COPY . .

RUN pip install -U pip && \
    pip install poetry && \
    poetry export --without-hashes --format=requirements.txt > requirements.txt && \
    yes | pip uninstall poetry && \
    pip install -r requirements.txt
