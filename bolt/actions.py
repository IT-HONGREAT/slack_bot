from bolt.contexts import context_1
from bolt.main import app, Handler
from notion.app import notion


@app.message("hello")
def message_hello(message, say):

    say(text=f"Hey there <@{message['user']}>!")


@app.action("get_reservation")
def action_button_click(body, ack, say):
    ack()
    link = "https://www.notion.so/486b0c639daf40d89ba2538e7214e47f?v=e37566dd51e646c19291259ed17b4157"
    say(f"<@{body['user']['id']}> clicked the button,,,,{link}")


@app.action("create_reservation")
def action_button_click(body, ack, say):
    ack()
    notion.create_reservation(
        database_name="reservation",
        room="어스",
        title="팀 회의 등록",
        purpose="내부회의",
        start="2023-02-01T01:00:00",
        end="2023-02-02T16:00:00",
    )
    say(**context_1)


Handler.start()
