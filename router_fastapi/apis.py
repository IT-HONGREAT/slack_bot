from fastapi import APIRouter, HTTPException

from bolt_python.app import bolt_app
from bolt_python.utils import get_user_information
from router_fastapi.models import Alarm

router = APIRouter(
    prefix="/admin",
    responses={404: {"description": "Not found"}},
)


@router.post("/alarm")
async def alarm(alarm: Alarm):

    user_id = get_user_information(bolt_app.client.users_list(), client_user_email=alarm.user_email)
    if user_id:
        bolt_app.client.chat_postMessage(channel=user_id, text=f"{alarm.user_name}님이 {alarm.context}관련 내용을 입력했습니다.")
        return {"user_id": user_id}
    raise HTTPException(status_code=404, detail="유저를 찾을수 없습니다.")
