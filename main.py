from typing import Union

from fastapi import FastAPI

from envs import get_env
from notion.reservation import get_reservation

app = FastAPI()


@app.get("/reservation")
async def read_reservation():
    Notion = get_env().get("Notion")
    databaseId = get_env().get("databaseId")
    headers = {
        "Authorization": "Bearer " + Notion,
        "accept": "application/json",
        "Notion-Version": "2022-06-28",
        "content-type": "application/json",
    }
    response = get_reservation(databaseId, headers)

    return response
