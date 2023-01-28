import requests, json


def readDatabase(databaseId, headers):
    readUrl = f"https://api.notion.com/v1/databases/{databaseId}/query"

    res = requests.post(readUrl, headers=headers)
    print(res.status_code)

    data = res.json()
    with open("./db.json", "w", encoding="utf8") as f:
        json.dump(data, f, ensure_ascii=False)


token = "secret_zePW85K46bT85mfxJSafUaC41uaNTmjR8K26ttjmpYc"
# https://www.notion.so/94ba17207ec24776b4279ffa89f0cbc4?v=a7c2a7ffec0f4b92b324cae50aa9a7db
databaseId = "94ba17207ec24776b4279ffa89f0cbc4"


headers = {
    "Authorization": "Bearer " + token,
    "Notion-Version": "2022-02-22"
}

readDatabase(databaseId, headers)