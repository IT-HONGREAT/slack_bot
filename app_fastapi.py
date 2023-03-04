from fastapi import FastAPI, HTTPException, APIRouter
from slack_bolt.adapter.asgi import SlackRequestHandler

from bolt.app import bolt_app
from bolt.utils import get_user_id
from router_fastapi.models import Alarm

# TODO
"""

fastapi의 apirouter 적용으로 flask의 blueprint처럼 활용가능한지 확인.

fastapi call 시 slack app call 되는점을 이용할것.
    slack api call 시 event handle이 안되는 점 파악하고 개선할것. 

"""


api = FastAPI()
app_handler = SlackRequestHandler(bolt_app)

# api_router = APIRouter()


@api.post("/alarm")
async def alarm(alarm: Alarm):

    check = bolt_app.client.users_list()
    user_id = get_user_id(check, user_email=alarm.user_email)
    if user_id:
        bolt_app.client.chat_postMessage(channel=user_id, text=f"{alarm.user_name}님이 {alarm.context}관련 내용을 입력했습니다.")
        return {"user_id": user_id}
    raise HTTPException(status_code=404, detail="유저를 찾을수 없습니다.")


# uvicorn 모듈이름:api --reload --port 3000 --log-level warning
