from settings import PlatFormSetting


class Slack(PlatFormSetting):
    def __init__(self):
        super().__init__()
        self.slack_bot_token = self.get_slack_detail_key("bot_token")
        self.slack_app_token = self.get_slack_detail_key("app_token")


slack_setting = Slack()
#
# app = Slack()
# test.setting()

# TODO result => app = App(token=??)
#
#
# test = Slack()
# test.post_message(
#     channel="#tokbottest",
#     blocks=[
#         {
#             "type": "section",
#             "text": {
#                 "type": "mrkdwn",
#                 "text": "*Approval Request*\nYour approval is requested to make an offer to <http://example.com|Florence Tran>.",
#             },
#         },
#         {"type": "context", "elements": [{"type": "mrkdwn", "text": "<http://example.com|View applicant>"}]},
#         {
#             "type": "actions",
#             "elements": [
#                 {"type": "button", "text": {"type": "plain_text", "text": "Approve", "emoji": True}},
#                 {"type": "button", "text": {"type": "plain_text", "text": "Reject", "emoji": True}},
#                 {"type": "button", "text": {"type": "plain_text", "text": ":robot_face:", "emoji": True}},
#             ],
#         },
#     ],
# )
