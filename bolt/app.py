from typing import List

from slack_bolt import App

from settings import PlatformSetting


class Slack(PlatformSetting):
    def __init__(self, tokens: List[str]):
        """
        If you need to add some token or secret_key for [slack or bolt] setup, add it here.

        If there is a better way, please suggest to in-yeong.
        """
        super().__init__()
        for token_name in tokens:
            setattr(self, f"slack_{token_name}", self.get_slack_detail_key(f"{token_name}"))


slack_setting = Slack(
    tokens=[
        "bot_token",
        "app_token",
        "signing_secret",
    ]
)
bolt_app = App(
    token=slack_setting.slack_bot_token,
    signing_secret=slack_setting.slack_signing_secret,
)
