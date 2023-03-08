from asyncio import sleep
from datetime import datetime

from fastapi import APIRouter, HTTPException

from bolt_python.app import bolt_app
from bolt_python.utils import get_user_information
from router_fastapi.models import Alarm, ContractSettlement

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


@router.post("/contract_settlement_alarm")
async def contract_management_alarm(contract_settlement: ContractSettlement):
    users = bolt_app.client.users_list()
    await sleep(1)

    today_check = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f":white_check_mark:{i.today_contract_management_project_name}] {i.today_payment_kind} (₩{'{:,}'.format(i.today_amount)}",
            },
        }
        for i in contract_settlement.today_alarm_projects
    ]

    next_check = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f":white_check_mark:{i.next_week_paid_date} [{i.next_week_contract_management_project_name}] {i.next_week_payment_kind} (₩{'{:,}'.format(i.next_week_amount)})",
            },
        }
        for i in contract_settlement.next_week_projects
    ]
    delay_check = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f":white_check_mark:[{i.delay_contract_management_project_name}] (₩{'{:,}'.format(i.delay_amount)}) : {i.delay_reason} )",
            },
        }
        for i in contract_settlement.delay_projects
    ]

    user_id = get_user_information(users, client_user_email=contract_settlement.user_email)
    user_name = get_user_information(users, client_user_id=user_id)
    today = datetime.now().strftime("%m월 %d일")
    if user_id:
        bolt_app.client.chat_postMessage(
            channel=user_id,
            text="금일 정산 알림이 도착했습니다",
            blocks=[
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": f"안녕하세요 :wave: {user_name}님!! {today} 정산일정 공유드립니다.:money_with_wings:",
                        "emoji": True,
                    },
                },
                {"type": "divider"},
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f":one:*[금일 예정 프로젝트]*\n",
                    },
                },
                *today_check,
                {"type": "divider"},
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f":two:*[차주 정산 예정 프로젝트]*\n",
                    },
                },
                *next_check,
                {"type": "divider"},
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f":three:*[지급 지연 프로젝트]*\n",
                    },
                },
                *delay_check,
            ],
        )
        return {"user_id": user_id}
    raise HTTPException(status_code=404, detail="유저를 찾을수 없습니다.")
