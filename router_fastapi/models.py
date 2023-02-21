from pydantic import BaseModel


class Alarm(BaseModel):
    user_name: str | None = None
    user_email: str
    context: str | None = None
    is_schedule: bool | None = None


class TempTesk(BaseModel):
    contract_name: str
    contract_money: int
