from slack_bolt.adapter.socket_mode import SocketModeHandler

from bolt_main import app, notion
from slack_mod.app import slack_setting


@app.message("hello")
def message_hello(message, say):
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
def message_bot(message, say):
    say(
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Approval Request*\nYour approval is requested to make an offer to <http://example.com|Florence Tran>.",
                },
            },
            {"type": "context", "elements": [{"type": "mrkdwn", "text": "<http://example.com|View applicant>"}]},
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "테이블링 예약조회", "emoji": True},
                        "action_id": "get_reservation",
                    },
                    {"type": "button", "text": {"type": "plain_text", "text": "Reject", "emoji": True}},
                    {"type": "button", "text": {"type": "plain_text", "text": ":robot_face:", "emoji": True}},
                ],
            },
        ],
    )


@app.action("get_reservation")
def action_button_click(body, ack, say):
    # Acknowledge the action
    ack()
    response = notion.get_reservation(database_name="reservation")
    say(f"<@{body['user']['id']}> clicked the button,,,,{response}")


SocketModeHandler(app, slack_setting.slack_app_token).start()
