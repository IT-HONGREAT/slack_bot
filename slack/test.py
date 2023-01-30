import slack_sdk

from envs import get_env

client = slack_sdk.WebClient(token=get_env().get("slack_token"))

client.chat_postMessage(channel="#tokbottest", text="hellow world!!")
