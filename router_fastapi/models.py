from typing import List, Union

from pydantic import BaseModel, Field


class Alarm(BaseModel):
    user_name: str = Field()
    user_email: str = Field()
    context: str | None = Field()
    is_schedule: bool | None = Field()


class TodayAlarmProjects(BaseModel):
    today_contract_management_project_name: str = Field()
    today_payment_kind: str = Field()
    today_amount: str = Field()


class NextWeekProjects(BaseModel):
    next_week_paid_date: str = Field()
    next_week_contract_management_project_name: str = Field()
    next_week_payment_kind: str = Field()
    next_week_amount: str = Field()


class DelayProjects(BaseModel):
    delay_contract_management_project_name: str = Field()
    delay_payment_kind: str = Field()
    delay_amount: str = Field()
    delay_reason: str = Field()


class ContractSettlement(BaseModel):
    user_email: str = Field()

    today_alarm_projects: Union[List[TodayAlarmProjects]] = Field()
    next_week_projects: Union[List[NextWeekProjects]] = Field()
    delay_projects: Union[List[DelayProjects]] = Field()
