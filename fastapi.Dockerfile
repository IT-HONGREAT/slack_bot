FROM python:3.10
MAINTAINER hongreat95@gmail.com

RUN mkdir /slackbot
WORKDIR /slackbot

ADD . /slackbot
RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8080
CMD ["uvicorn","app_fastapi:api","--reload","--host","0.0.0.0","--port","8080"]
