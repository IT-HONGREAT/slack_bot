from typing import Union

from fastapi import FastAPI

from envs import get_env
from notion.reservation import get_reservation

app = FastAPI()


@app.get("/reservation")
async def read_reservation():
    notion_token = get_env().get("notion_token")
    databaseId = get_env().get("databaseId")
    headers = {
        "Authorization": "Bearer " + notion_token,
        "accept": "application/json",
        "Notion-Version": "2022-06-28",
        "content-type": "application/json",
    }
    response = get_reservation(databaseId, headers)

    return response
