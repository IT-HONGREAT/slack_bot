from envs import get_env
from notion.reservation import get_reservation, create_reservation

notion_token = get_env().get("notion_token")
databaseId = get_env().get("databaseId")
headers = {
    "Authorization": "Bearer " + notion_token,
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
