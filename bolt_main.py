import dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from notion.app import Notion
from settings import BASE_DIR

notion = Notion()


bot_token = dotenv.get_key(
    dotenv_path=f"{BASE_DIR}/.env",
    key_to_get=f"SLACK_BOT_TOKEN",
)
app_token = dotenv.get_key(
    dotenv_path=f"{BASE_DIR}/.env",
    key_to_get=f"SLACK_APP_TOKEN",
)
app = App(token=bot_token)


@app.message("hello")
def message_hello(message, say):
    print("message", message)
    say(f"Hey there <@{message['user']}>!")


SocketModeHandler(app, app_token).start()
