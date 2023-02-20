from slack_bolt.adapter.socket_mode import SocketModeHandler

# from bolt.app import slack_setting, app
from bolt.app import slack_setting, bolt_app
from bolt.utils import make_button_blocks

""""""

# TODO : Make settings class or functions.
# If there is a better way, please suggest to in-yeong.

button_settings = {
    "https://www.notion.so/toktokhan/TOKTOKHAN-DEV-2f9699f43a3e402ebe6713f0eaf27325": ":partying_face: 회의실예약 노션 링크(temp_toknotion)",
    "create_reservation": ":call_me_hand: 회의실 예약하기",
    "get_lunch_menu": ":knife_fork_plate: 점메추",
}


bot_button = make_button_blocks(button_settings)


@bolt_app.event("app_mention")
def main_bot(message, say):
    """
    Main Bot

    1. Add your action in "action_settings"
        key : value
        ex) <your-func-name> :  description

    2. Create your action function in "action.py"

    Slack

    1. set app_mention Subscribe to bot events

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
                "elements": bot_button,
            },
        ],
    )


# Handler = SocketModeHandler(bolt_app, slack_setting.slack_app_token)
bolt_socket_handler = SocketModeHandler(bolt_app, slack_setting.slack_app_token)
