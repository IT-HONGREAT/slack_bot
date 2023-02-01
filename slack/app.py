import slack_sdk

from settings import PlatFormSetting


class Slack(PlatFormSetting):
    def __init__(self):
        super().__init__()
        self.client = slack_sdk.WebClient(token=self.token)

    def post_message(self, channel, blocks):
        # self.client.chat_postMessage(channel="#tokbottest", text="hellow world!!")
        self.client.chat_postMessage(channel=channel, blocks=blocks)

    def reactions_add(self):
        self.client.reactions_add(channel="#tokbottest", name="thumbsup", timestamp="1234567890.123456")


test = Slack()
test.post_message(
    channel="#tokbottest",
    blocks=[
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*Approval Request*\nYour approval is requested to make an offer to <http://example.com|Florence Tran>.",
            },
        },
        {"type": "context", "elements": [{"type": "mrkdwn", "text": "<http://example.com|View applicant>"}]},
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
                        {"text": {"type": "plain_text", "text": "Activity feed", "emoji": True}, "value": "value-1"},
                        {"text": {"type": "plain_text", "text": "Details", "emoji": True}, "value": "value-3"},
                    ],
                },
            ],
        },
    ],
)
# test.reactions_add()
