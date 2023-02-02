from slack_bolt.adapter.socket_mode import SocketModeHandler

from bolt_main import app
from slack_mod.app import slack_setting


@app.message("hello")
async def message_hello(message, say):

    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Hey there <@{message['user']}>!"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Click Me"},
                    "action_id": "button_click",
                },
            }
        ],
        text=f"Hey there <@{message['user']}>!",
    )


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


@app.action("get_reservation")
def action_button_click(body, ack, say):
    # Acknowledge the action
    ack()
    # response = await notion.get_reservation(database_name="reservation")
    link = "https://www.notion.so/486b0c639daf40d89ba2538e7214e47f?v=e37566dd51e646c19291259ed17b4157"
    say(f"<@{body['user']['id']}> clicked the button,,,,{link}")


SocketModeHandler(app, slack_setting.slack_app_token).start()


# async def main():
#     handler = AsyncSocketModeHandler(
#         app, "xapp-1-A04M2K0CL3U-4749434184065-4add86b2becb7b83fd29efe0df35e64a2d9fc9ef5675c13980bc95924005a307"
#     )
#     await handler.start_async()


# asyncio.run(main())
