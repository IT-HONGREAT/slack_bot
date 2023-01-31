from typing import Optional

import requests, json

from envs import get_env
from settings import PlatFormSetting


class Notion(PlatFormSetting):
    def __init__(self):
        super().__init__()
        self.headers = {
            "Authorization": "Bearer " + self.token,
            "accept": "application/json",
            "Notion-Version": "2022-06-28",
            "content-type": "application/json",
        }

    # def temp_get_db_id(self, db_name):
    #     self.db_name = db_name
    #
    #     print("이름 확인하기!!!", self.db_name)
    #
    #     # print("new!?!?!?", self.db)
    #
    #     db_id = ""
    #     return db_id

    def _get_url(self, type: Optional[str] = "read", db_id=None):
        """
        :param type: read/create ex) "read"
        :param db_id:
        :return: url ex)https://~~~
        """
        if type == "read":
            url = f"https://api.notion.com/v1/databases/{db_id}/query"

        if type == "create":
            url = "https://api.notion.com/v1/pages"

        return url

    def get_reservation(self, database_name=None):  # TODO db종류(이름)로 변경
        # read_url = f"https://api.notion.com/v1/databases/{databaseId}/query"
        db_id = self.temp_get_db_id(database_name)  # TODO 여기서부터 확인가능~~!

        read_url = self._get_url(type="read", db_id=db_id)

        # TODO headers 도 합치기
        response = requests.post(read_url, headers=self.headers)
        data = response.json()
        data_result = data.get("results")
        for i in data_result:
            one_property = i.get("properties")

            room = one_property["방"]["select"]["name"]
            created_by = one_property["생성자"]["created_by"]["name"]
            title = one_property["제목"]["title"][0].get("plain_text")
            if one_property["이용시간"].get("date"):
                start = one_property["이용시간"].get("date").get("start")
                end = one_property["이용시간"].get("date").get("end")
            tag = one_property["용도"]["select"]["name"]

            print("방", "=>", room)
            print("생성자", "=>", created_by)
            print("제목", "=>", title)
            if one_property["이용시간"].get("date"):
                print("이용시간", "=>", start)
                print("이용시간", "=>", end)
            print("용도", "=>", tag)

        return {"status_code": response.status_code}


def create_reservation(
    databaseId,
    headers,
    room=None,
    title=None,
    purpose=None,
    start=None,
    end=None,
):
    createdUrl = "https://api.notion.com/v1/pages"

    newPageData = {
        "parent": {"database_id": databaseId},
        "properties": {
            "방": {
                "select": {
                    "name": room,
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
            "제목": {"title": [{"text": {"content": title}}]},
            "이용시간": {"date": {"start": start, "end": end}},
            "용도": {
                "select": {
                    "name": purpose,
                }
            },
        },
    }

    data = json.dumps(newPageData)
    response = requests.post(createdUrl, headers=headers, data=data)
    return {"status_code": response.status_code}
