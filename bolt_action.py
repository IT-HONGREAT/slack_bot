import asyncio

from slack_bolt.adapter.socket_mode.aiohttp import AsyncSocketModeHandler

from bolt_main import app


@app.message("hello")
async def message_hello(message, say):
    print("message", message)
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


@app.message("bot")
async def message_bot(message, say):
    await say(
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
                "elements": [
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "테이블링 예약조회", "emoji": True},
                        "action_id": "get_reservation",
                    },
                    {"type": "button", "text": {"type": "plain_text", "text": "테이블링 예약 생성", "emoji": True}},
                    {"type": "button", "text": {"type": "plain_text", "text": ":robot_face:", "emoji": True}},
                ],
            },
        ],
    )


@app.action("get_reservation")
async def action_button_click(body, ack, say):
    # Acknowledge the action
    await ack()
    # response = await notion.get_reservation(database_name="reservation")
    link = "https://www.notion.so/486b0c639daf40d89ba2538e7214e47f?v=e37566dd51e646c19291259ed17b4157"
    await say(f"<@{body['user']['id']}> clicked the button,,,,{link}")


# SocketModeHandler(app, slack_setting.slack_app_token).start()


# Add middleware / listeners here


async def main():
    handler = AsyncSocketModeHandler(
        app, "xapp-1-A04M2K0CL3U-4749434184065-4add86b2becb7b83fd29efe0df35e64a2d9fc9ef5675c13980bc95924005a307"
    )
    await handler.start_async()


asyncio.run(main())
