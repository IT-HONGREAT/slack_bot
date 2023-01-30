from pprint import pprint

import requests, json
from env import get_env
from reservation import get_reservation, create_reservation

token = get_env().get("token")
databaseId = get_env().get("databaseId")
headers = {
    "Authorization": "Bearer " + token,
    "accept": "application/json",
    "Notion-Version": "2022-06-28",
    "content-type": "application/json",
}


get_reservation(databaseId, headers)

create_reservation(
    databaseId,
    headers,
    room="어스",
    title="기타",
    purpose="미팅",
    start="2023-01-30T01:00:00",
    end="2023-01-30T16:00:00",
)
