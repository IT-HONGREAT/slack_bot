from fastapi import FastAPI
from slack_bolt.adapter.asgi import SlackRequestHandler

from api_models.temp_model import Alarm
from bolt.app import bolt_app

api = FastAPI()
app_handler = SlackRequestHandler(bolt_app)


@api.post("/alarm")
async def alarm(alarm: Alarm):

    print(alarm.user_name)
    print(alarm.context)
    print(alarm.is_schedule)

    return {"test":"teststetset"}
#
# @api.post("/some_test")
# async def some_logic(req: Request):
#     print("testtesttes!!")
#     # return await app_handler.handle(req)


# uvicorn app:api --reload --port 3000 --log-level warning
