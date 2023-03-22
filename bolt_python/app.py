from typing import List
from urllib.parse import urlparse

from slack_bolt import App

from settings import PlatformSetting


class Slack(PlatformSetting):
    NOTION_LINK = "https://www.notion.so/toktokhan/TOKTOKHAN-DEV-2f9699f43a3e402ebe6713f0eaf27325"
    EMOJI_PARTY = ":partying_face:"
    EMOJI_HAND = ":call_me_hand:"
    EMOJI_FOOD = ":knife_fork_plate:"
    EMOJI_LETTER = ":love_letter:"
    EMOJI_ALARM = ":alarm_clock:"
    EMOJI_WAVE = ":wave:"
    EMOJI_WHITE_CHECK_MARK = ":white_check_mark:"
    EMOJI_ONE = ":one:"
    EMOJI_TWO = ":two:"
    EMOJI_THREE = ":three:"
    EMOJI_MONEY_WITH_WINGS = ":money_with_wings:"
    EMOJI_SPEAKING_HEAD_IN_SILHOUETTE = ":speaking_head_in_silhouette:"

    BUTTON_SETTINGS = {
        NOTION_LINK: f"{EMOJI_PARTY} 회의실예약 노션 링크(temp_toknotion)",
        "create_reservation": f"{EMOJI_HAND} 회의실 예약하기",
        "get_lunch_menu": f"{EMOJI_FOOD} 점메추",
        "send_dm_anonymous": f"{EMOJI_LETTER} 마음의 편지",
        "send_dm_schedule": f"{EMOJI_ALARM} 예약 메세지",
        "send_anonymous_board": f"{EMOJI_SPEAKING_HEAD_IN_SILHOUETTE} 익명으로 게시하기",
    }

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

    @property
    def function_button(self):
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
            for some_value, description in self.BUTTON_SETTINGS.items()
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
