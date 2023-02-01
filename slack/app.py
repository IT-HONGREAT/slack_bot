import slack_sdk

from settings import PlatFormSetting


class Slack(PlatFormSetting):
    def __init__(self):
        super().__init__()
        self.client = slack_sdk.WebClient(token=self.token)

    def main_bot(self, channel, blocks):
        self.client.chat_postMessage(channel=channel, blocks=blocks)

    def post_message(self, channel, text):
        self.client.chat_postMessage(channel="#tokbottest", text="hellow world!!")


test = Slack()

block_form = [
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*TokBot*\n 사용하고싶은 기능을 눌러주세요~~.",
        },
    },
    {"type": "context", "elements": [{"type": "mrkdwn", "text": "<http://www.naver.com|naver메인>"}]},
    {
        "type": "actions",
        "elements": [
            {"type": "button", "text": {"type": "plain_text", "text": "Approve", "emoji": True}},
            {"type": "button", "text": {"type": "plain_text", "text": "Reject", "emoji": True}},
            {"type": "button", "text": {"type": "plain_text", "text": ":robot_face:", "emoji": True}},
            {
                "type": "overflow",
                "options": [
                    {"text": {"type": "plain_text", "text": "Follow", "emoji": True}, "value": "value-0"},
                    {"text": {"type": "plain_text", "text": "Activity feed", "emoji": True}, "value": "value-2"},
                    {"text": {"type": "plain_text", "text": "Details", "emoji": True}, "value": "value-1"},
                ],
            },
        ],
    },
]

test.main_bot(
    channel="#tokbottest",
    blocks=block_form,
)
# test.reactions_add()
