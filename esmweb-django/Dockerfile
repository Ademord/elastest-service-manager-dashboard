# ademord/esmweb
FROM python:3.6

RUN apt-get update -qq && apt-get install -qy netcat
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
CMD python manage.py runserver 0.0.0.0:8000