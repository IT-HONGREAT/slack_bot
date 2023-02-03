from bolt.contexts import context_example
from bolt.main import app, Handler


@app.message("hello")
def message_hello(message, say):
    say(text=f"Hey there <@{message['user']}>!")


@app.action("get_reservation")
def test_name(body, ack, say):
    ack()
    say(context_example)


Handler.start()
