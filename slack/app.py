import slack_sdk

from settings import PlatFormSetting


class Slack(PlatFormSetting):
    def __init__(self):
        super().__init__()
        self.client = slack_sdk.WebClient(token=self.token)

    def post_message(self):
        self.client.chat_postMessage(channel="#tokbottest", text="hellow world!!")


test = Slack()
