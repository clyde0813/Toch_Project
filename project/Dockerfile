FROM python:3.9
ENV PYTHONUNBUFFERED = 1

RUN apt-get update && apt-get install -y python3-pip
WORKDIR /app
RUN mkdir /app/django-server
ADD . /app/django-server

WORKDIR /app/django-server

RUN pip install -r requirements.txt

RUN python3 manage.py collectstatic --noinput