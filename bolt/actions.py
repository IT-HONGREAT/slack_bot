from bolt.contexts import context_example
from bolt.main import app, Handler
from notion.temp_actions import temp_dired_action_function


@app.message("hello")
def message_hello(message, say):
    say(text=f"Hey there <@{message['user']}>!")


@app.action("get_reservation")
def get_(body, ack, say):
    ack()
    say(context_example)


@app.action("create_reservation")
def make_reservation(body, ack, say):
    ack()
    check = temp_dired_action_function(
        database_name="reservation",
        room="어스",
        title="팀 회의",
        start="2023-02-02T01:00:00",
        end="2023-02-03T01:00:00",
        purpose="기타",
    )
    say({"text": f"생성됨{check}"})


bolt_socket = Handler.start()
