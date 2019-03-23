FROM python:3.6-alpine

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .

RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev && \
    pip install -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000