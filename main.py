from typing import Union

from fastapi import FastAPI

from envs import get_env
from notion.reservation import Notion

app = FastAPI()
# TODO 1. 엔드포인트에서 플랫폼 클래스를 호출하도록
notion = Notion()


@app.get("/reservation")
async def read_reservation():
    databaseId = get_env().get("databaseId")

    response = notion.get_reservation(databaseId)
    # TODO 2. db종류(이름) 은 함수단위로 받아야할듯.
    response = notion.get_reservation(database_name="reservation_db")
    print("???")
    return response


# TODO test
response = notion.get_reservation(database_name="reservation_db")
