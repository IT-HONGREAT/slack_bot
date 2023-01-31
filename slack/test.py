import slack_sdk

from envs import get_env

client = slack_sdk.WebClient(token=get_env().get("Slack"))

client.chat_postMessage(channel="#tokbottest", text="hellow world!!")
