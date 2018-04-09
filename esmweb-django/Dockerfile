FROM python:3.4

RUN apt-get update -qq && apt-get install -qy netcat
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
