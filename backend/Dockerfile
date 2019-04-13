FROM python:3.7-alpine

RUN mkdir /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY ./app/ /app
WORKDIR /app

RUN adduser -D user
USER user
