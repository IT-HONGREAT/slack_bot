FROM python:3.10
MAINTAINER hongreat95@gmail.com

RUN mkdir /slackbot
WORKDIR /slackbot

ADD . /slackbot

ENV NOTION $NOTION
ENV SLACK_APP_TOKEN $SLACK_APP_TOKEN
ENV SLACK_BOT_TOKEN $SLACK_BOT_TOKEN
ENV SLACK_SIGNING_SECRET $SLACK_SIGNING_SECRET
ENV NOTION_reservation $NOTION_reservation
ENV NOTION_lunch $NOTION_lunch
# Run Slackbot Secrets
RUN echo "NOTION=$NOTION" >> .env && \
    echo "SLACK_APP_TOKEN=$SLACK_APP_TOKEN" >> .env && \
    echo "SLACK_BOT_TOKEN=$SLACK_BOT_TOKEN" >> .env && \
    echo "SLACK_SIGNING_SECRET=$SLACK_SIGNING_SECRET" >> .env && \
    echo "NOTION_reservation=$NOTION_reservation" >> .env && \
    echo "NOTION_lunch=$NOTION_lunch" >> .env

RUN pip install --upgrade pip && pip install -r requirements.txt
ENTRYPOINT ["python","main.py"]
