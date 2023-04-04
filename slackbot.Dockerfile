FROM python:3.10-slim-buster AS build
MAINTAINER hongreat95@gmail.com

RUN mkdir /slackbot
WORKDIR /slackbot

ADD . /slackbot

ARG NOTION
ARG SLACK_APP_TOKEN
ARG SLACK_BOT_TOKEN
ARG SLACK_SIGNING_SECRET
ARG NOTION_reservation
ARG NOTION_lunch

RUN chmod +x setup_env.sh && ./setup_env.sh

RUN pip install --upgrade pip && \
    pip install --no-cache-dir --target=/install -r requirements.txt

# Production stage
FROM python:3.10-slim-buster AS production

RUN mkdir /slackbot
WORKDIR /slackbot

COPY --from=build /install /usr/local/lib/python3.10/site-packages/
COPY . /slackbot

ENTRYPOINT ["python","main.py"]

