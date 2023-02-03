from slack_bolt import App

from notion_api.app import Notion
from slack_api.app import slack_setting

notion = Notion()
app = App(token=slack_setting.slack_bot_token)


action_settings = {
    "get_reservation": ":one: 테이블링 예약조회",
    "create_reservation": ":two: 테이블 예약생성",
}


action_list = [
    {
        "type": "button",
        "text": {"type": "plain_text", "text": value, "emoji": True},
        "action_id": key,
    }
    for key, value in action_settings.items()
]


@app.message("bot")
def message_bot(message, say):
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
