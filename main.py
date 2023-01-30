from pprint import pprint

import requests, json
from env import get_env


def readDatabase(databaseId, headers):
    readUrl = f"https://api.notion.com/v1/databases/{databaseId}/query"

    # payload = {"page_size": 100}
    # response = requests.post(readUrl, json=payload, headers=headers)
    response = requests.post(readUrl, headers=headers)
    print(response.status_code)
    data = response.json()
    # with open("./db.json", "w", encoding="utf8") as f:
    #     json.dump(data, f, ensure_ascii=False)

    # pprint(data)
    # pprint(type(data))
    data_result = data.get("results")
    pprint(data_result)
    for i in data_result:
        one_property = i.get("properties")
        print("=====" * 50)
        print("방", "=>", one_property["방"])
        print("방", "=>", one_property["방"]["select"]["name"])
        print("생성자", "=>", one_property["생성자"])
        print("생성자", "=>", one_property["생성자"]["created_by"]["name"])
        print("이름", "=>", one_property["이름"])
        print("이름", "=>", one_property["이름"]["title"][0].get("plain_text"))
        print("이용시간", "=>", one_property["이용시간"])
        if one_property["이용시간"].get("date"):
            print("이용시간", "=>", one_property["이용시간"].get("date").get("start"))
            print("이용시간", "=>", one_property["이용시간"].get("date").get("end"))
        print("태그", "=>", one_property["태그"])
        print("태그", "=>", one_property["태그"]["select"]["name"])
        # for j in one_property:

    # print(data_result)


token = get_env().get("token")
databaseId = get_env().get("databaseId")
headers = {
    "Authorization": "Bearer " + token,
    "accept": "application/json",
    "Notion-Version": "2022-06-28",
    "content-type": "application/json",
}

# readDatabase(databaseId, headers)


"""
---
"""

import requests, json


def createPage(databaseId, headers):
    createdUrl = "https://api.notion.com/v1/pages"

    newPageData = {
        "parent": {"database_id": databaseId},
        "properties": {
            "방": {
                "select": {
                    "name": "지니",
                },
            },
            # "생성자": {
            #     "created_by": {
            #         "name": "홍인영",
            #         "object": "user",
            #         "person": {"email": "iyiy95@naver.com"},
            #     },
            #     "type": "created_by",
            # },
            "이름": {"title": [{"text": {"content": "이름확인!!!"}}]},
            # "이용시간": {"date": {"end": "2023-01-30T16:00:00.000+09:00", "start": "2023-01-30T00:00:00.000+09:00"}},
            "태그": {
                "select": {
                    "name": "내부회의",
                    # "color": "orange",
                }
            },
        },
    }

    data = json.dumps(newPageData)

    res = requests.post(createdUrl, headers=headers, data=data)

    with open("./db.json", "w", encoding="utf8") as f:
        json.dump(data, f, ensure_ascii=False)
    print(res.status_code)


# token = "{Your Private API Token}"
#
# databaseId = "{Your DatabaseID}"

headers = {"Authorization": "Bearer " + token, "Content-Type": "application/json", "Notion-Version": "2022-02-22"}


createPage(databaseId, headers)
