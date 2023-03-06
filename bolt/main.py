from bolt.app import bolt_app
from bolt.utils import make_button_blocks

# Slack Emoji
NOTION_LINK = "https://www.notion.so/toktokhan/TOKTOKHAN-DEV-2f9699f43a3e402ebe6713f0eaf27325"
EMOJI_PARTY = ":partying_face:"
EMOJI_HAND = ":call_me_hand:"
EMOJI_FOOD = ":knife_fork_plate:"
EMOJI_LETTER = ":love_letter:"
EMOJI_ALARM = ":alarm_clock:"

BUTTON_SETTINGS = {
    NOTION_LINK: f"{EMOJI_PARTY} 회의실예약 노션 링크(temp_toknotion)",
    "create_reservation": f"{EMOJI_HAND} 회의실 예약하기",
    "get_lunch_menu": f"{EMOJI_FOOD} 점메추",
    "send_dm_anonymous": f"{EMOJI_LETTER} 마음의 편지",
    "send_dm_schedule": f"{EMOJI_ALARM} 예약 메세지",
}

bot_buttons = make_button_blocks(BUTTON_SETTINGS)


@bolt_app.event("app_mention")
def handle_app_mention(message: dict, say: callable) -> None:
    """
    Handles @mention event in Slack
    """
    say(
        blocks=[
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": ":information_desk_person: slack bot",
                    "emoji": True,
                },
            },
            {"type": "context", "elements": [{"type": "mrkdwn", "text": "<http://naver.com|ex-naver link>"}]},
            {
                "type": "actions",
                "elements": bot_buttons,
            },
        ],
    )


main_button_check = "bolt main button is called!"  # instead handler | call check
