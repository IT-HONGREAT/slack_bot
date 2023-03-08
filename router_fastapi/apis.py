from datetime import datetime
from typing import List

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
async def contract_management_alarm(contract_settlement: List[ContractSettlement]):

    user_id = get_user_information(bolt_app.client.users_list(), client_user_email=contract_settlement.user_email)

    today = datetime.now().strftime("%Y년 %m월 %d일")
    if user_id:
        # bolt_app.client.chat_postMessage(
        #     channel=user_id,
        #     blocks=[
        #         {
        #             "type": "section",
        #             "text": {
        #                 "type": "mrkdwn",
        #                 "text": f"안녕하세요 ^^ {contract.user_email}님!! {today} 정산일정 공유드립니다."
        #                 f"*[금일 정산 예정 프로젝트]* ₩{contract.today_amount}"
        #                 f"{contract.today_contract_management_project_name} 잔금 ₩{contract.today_amount}"
        #                 f"{contract.today_payment_kind}"
        #                 f"*[차주 전체 정산 예정 프로젝트]* ₩{contract.next_week_amount}"
        #                 f"{contract.next_week_paid_date} {contract.next_week_contract_management_project_name} 선금(₩{{contract.next_week_amount}})"
        #                 f"{contract.next_week_payment_kind}"
        #                 f"*[지급 지연 프로젝트]* 총 ₩{contract.delay_amount}(Todo)"
        #                 f"* {contract.delay_contract_management_project_name} 잔금 ₩{contract.delay_amount} : {contract.delay_reason}",
        #             },
        #         }
        #     ],
        # )
        return {"user_id": user_id}
    raise HTTPException(status_code=404, detail="유저를 찾을수 없습니다.")
