from pydantic import BaseModel


class Alarm(BaseModel):
    user_name: str
    user_email: str
    context: str
    is_schedule: bool


class TempTesk(BaseModel):
    contract_name: str
    contract_money: int
