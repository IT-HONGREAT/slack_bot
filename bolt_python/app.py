from typing import List, Union
from urllib.parse import urlparse

from slack_bolt import App

from settings import PlatformSetting

ANONYMOUS_BOARD_CHANNEL = "C050C70HFHN"
BOT_OWN_CHANNEL = "C04QK0W6072"


class Slack(PlatformSetting):
    def __init__(self, tokens: List[str]):
        """
        If you need to add some token or secret_key for [slack or bolt_python] setup, add it here.

        If there is a better way, please suggest to @IT-HONGREART.
        """
        super().__init__()
        for token_name in tokens:
            setattr(self, f"slack_{token_name}", self.get_slack_detail_key(f"{token_name}"))

    @staticmethod
    def check_direct_link(url):
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False

    def remote_function_button(self, bot_kind=Union[dict[str, str]]):
        dict_to_list = [
            {
                "type": "button",
                "text": {"type": "plain_text", "text": description, "emoji": True},
                "url": some_value,
            }
            if self.check_direct_link(some_value)
            else {
                "type": "button",
                "text": {"type": "plain_text", "text": description, "emoji": True},
                "action_id": some_value,
            }
            for some_value, description in bot_kind.items()
        ]
        return dict_to_list


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
