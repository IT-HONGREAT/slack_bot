from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from bolt.app import slack_setting

# notion = Notion()
app = App(token=slack_setting.slack_bot_token)


# TODO : Make settings class or functions.
# If there is a better way, please suggest to in-yeong.
action_settings = {
    "get_reservation": ":one: 테이블링 예약조회",
    "create_reservation": ":two: 테이블 예약생성",
}


action_list = [
    {
        "type": "button",
        "text": {"type": "plain_text", "text": description, "emoji": True},
        "action_id": some_action,
    }
    for some_action, description in action_settings.items()
]


@app.message("bot")
def message_bot(message, say):
    """
    Main Bot

    1. Add your action in "action_settings"
        key : value
        ex) <your-func-name> :  description

    2. Create your action function in "action.py"
    """
    say(
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*똑봇 테스트*\n 아아 테스트 중입니다. <http://naver.com|네이버 메인!>.",
                },
            },
            {"type": "context", "elements": [{"type": "mrkdwn", "text": "<http://kakao.com|ㅋㅋㅋㅋ>"}]},
            {
                "type": "actions",
                "elements": action_list,
            },
        ],
    )


Handler = SocketModeHandler(app, slack_setting.slack_app_token)
