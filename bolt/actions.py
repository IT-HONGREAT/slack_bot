from bolt.contexts import context_example
from bolt.main import app, Handler
from notion.actions import example_action_function


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
    check = example_action_function(
        database_name="<your-db-name>",  # check NOTION_{DB_NAME} in <.env>
        # example_text="제목"
        # example_dt="2023-02-03T01:00:00",
    )
    say({"text": f"생성됨{check}"})


bolt_socket = Handler.start()
