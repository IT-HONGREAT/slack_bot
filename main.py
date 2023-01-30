import requests, json
from env import get_env


def readDatabase(databaseId, headers):
    readUrl = f"https://api.notion.com/v1/databases/{databaseId}/query"

    payload = {"page_size": 100}
    response = requests.post(readUrl, json=payload, headers=headers)
    print(response.status_code)
    data = response.json()
    with open("./db.json", "w", encoding="utf8") as f:
        json.dump(data, f, ensure_ascii=False)


token = get_env().get("token")
databaseId = get_env().get("databaseId")
headers = {
    "Authorization": "Bearer " + token,
    "accept": "application/json",
    "Notion-Version": "2022-06-28",
    "content-type": "application/json",
}

readDatabase(databaseId, headers)
