FROM python:3.10
MAINTAINER hongreat95@gmail.com

RUN mkdir /slackbot
WORKDIR /slackbot

ADD . /slackbot

# Use Gitsecrets
ARG NOTION
ARG SLACK_APP_TOKEN
ARG SLACK_BOT_TOKEN
ARG SLACK_SIGNING_SECRET
ARG NOTION_reservation
ARG NOTION_lunch

RUN chmod +x setup_env.sh && ./setup_env.sh

RUN pip install --upgrade pip && pip install -r requirements.txt
ENTRYPOINT ["python","main.py"]
