# syntax=docker/dockerfile:1

FROM python:3.11-slim-buster

WORKDIR /python-docker

COPY . .
RUN pip3 install -r requirements.txt


ENV FLASK_APP=run.py
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]