from pydantic import BaseModel, Field


class Alarm(BaseModel):
    user_name: str = Field(alias="userName")
    user_email: str = Field(alias="userEmail")
    context: str | None = Field(alias="context")
    is_schedule: bool | None = Field(alias="isSchedule")


class ContractManagement(BaseModel):

    user_email: str = Field(alias="userEmail")

    today_contract_management_project_name: str = Field(alias="todayContractManagementProjectName")
    today_payment_kind: int = Field(alias="todayPaymentKind")
    today_amount: int = Field(alias="todayAmount")

    next_week_paid_date: str = Field(alias="nextWeekPaidDate")
    next_week_contract_management_project_name: str = Field(alias="nextWeekContract_managementProjectName")
    next_week_payment_kind: str = Field(alias="nextWeekPaymentKind")
    next_week_amount: int = Field(alias="nextWeekAmount")

    delay_contract_management_project_name: str = Field(alias="delayContractManagementProjectName")
    delay_payment_kind: str = Field(alias="delayPaymentKind")
    delay_amount: str = Field(alias="delayAmount")
    delay_reason: str = Field(alias="delayReason")
