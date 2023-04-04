from bolt_python.app import bolt_app, slack_setting, BOT_OWN_CHANNEL
from bolt_python.contexts import GUIDE_BOT, MAIN_BOT


@bolt_app.shortcut("call_guide_bot")
def call_guide_shortcut(client, ack):
    """
    Call Guide buttons of other bot
    """
    ack()
    client.chat_postMessage(
        channel=BOT_OWN_CHANNEL,
        blocks=[
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": ":rocket: 슬랙봇 가이드",
                    "emoji": True,
                },
            },
            {
                "type": "context",
                "elements": [
                    {"type": "mrkdwn", "text": "어떤 앱들이 있는지 알려주는 가이드앱 입니다."},
                ],
            },
            {"type": "divider"},
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f":one: 메인 봇을 호출 합니다.",
                },
            },
            {
                "type": "context",
                "elements": [
                    {"type": "mrkdwn", "text": "회의실 예약하기, 점심 메뉴추천, 예약 메세지, 똑개 대나무숲 등이 있습니다."},
                ],
            },
            {
                "type": "actions",
                "elements": slack_setting.remote_function_button(GUIDE_BOT),
            },
        ],
    )


@bolt_app.shortcut("call_main_bot")
def main_bot_shortcut(client, ack):
    ack()
    client.chat_postMessage(
        channel=BOT_OWN_CHANNEL,
        blocks=[
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": ":information_desk_person: slack bot",
                    "emoji": True,
                },
            },
            {"type": "context", "elements": [{"type": "mrkdwn", "text": "<http://google.com|ex-google link>"}]},
            {
                "type": "actions",
                "elements": slack_setting.remote_function_button(MAIN_BOT),
            },
        ],
    )


@bolt_app.action("call_main_bot")
@bolt_app.event("app_mention")
def handle_app_mention(message: dict, say: callable) -> None:
    """
    Call main bot buttons
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
                "elements": slack_setting.remote_function_button(MAIN_BOT),
            },
        ],
    )


main_button_check = "🧑🏻‍💻 bolt_python main button is called!"  # instead handler | call check
