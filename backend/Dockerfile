# Base for both service and test images
FROM python:3.7-alpine as back_base

RUN mkdir /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
COPY ./app/ /app
WORKDIR /app

# Service image
FROM back_base AS back

RUN adduser -D user
USER user

# Test image
FROM back_base AS back_test

COPY ./testing.txt /app/testing.txt
RUN pip install -r /app/testing.txt