FROM python:3.10
MAINTAINER hongreat95@gmail.com

RUN mkdir /slackbot
WORKDIR /slackbot

ADD . /slackbot


RUN echo "NOTION=$NOTION" >> .env
RUN echo "SLACK_APP_TOKEN=$SLACK_APP_TOKEN" >> .env
RUN echo "SLACK_BOT_TOKEN=$SLACK_BOT_TOKEN" >> .env
RUN echo "SLACK_SIGNING_SECRET=$SLACK_SIGNING_SECRET" >> .env
RUN echo "NOTION_reservation=$NOTION_reservation" >> .env
RUN echo "NOTION_lunch=$NOTION_lunch" >> .env

RUN cat .env



RUN pip install --upgrade pip && pip install -r requirements.txt
ENTRYPOINT ["python","main.py"]
