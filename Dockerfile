FROM python:3.8

WORKDIR /usr/src/fastapi-blog

COPY ./src/blog ./src

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt