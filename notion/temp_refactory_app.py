import json
from typing import Optional

import requests

from settings import PlatFormSetting


class Notion(PlatFormSetting):
    # Add some notion settings here.
    def __init__(self):
        super().__init__()
        self.headers = {
            "Authorization": "Bearer " + self.token,
            "accept": "application/json",
            "Notion-Version": "2022-06-28",
            "content-type": "application/json",
        }

    def _get_url(self, type: Optional[str] = "read_db", database_id=None):
        """
        :param type: read/create ex) "read"
        :param database_id:
        :return: url ex)https://~~~
        """

        temp_mapping = {
            "read_db": f"https://api.notion.com/v1/databases/{database_id}/query",
            "create_page": "https://api.notion.com/v1/pages",
        }

        return temp_mapping.get(type)

    # TODO read, create 함수 분기

    async def get_db(self, database_name=None):

        read_url = self._get_url(type="read_db", database_id=self.get_database_id(database_name))

        response = requests.post(read_url, headers=self.headers)
        data = response.json()
        data_result = data.get("results")

        for i in data_result:
            print("<your data_result> ")

        return {"status_code": data.status_code}

    # TODO read, create 함수 분기

    def create_page(self, database_name=None):
        database_id = self.get_database_id(database_name)
        create_page_url = self._get_url(type="create_page", database_id=database_id)

        return {
            "database_id": database_id,
            "create_page_url": create_page_url,
        }

    def temp_create_some_page_data(self, data_example_1=None):
        temp = self.create_page(database_name="create_reservation")

        new_page_data = {
            "parent": {"database_id": temp.get("database_id")},
            # "properties":"<your-data-format>",
            "properties": {
                "방": {
                    "select": {
                        "name": room,
                    },
                },
                "제목": {"title": [{"text": {"content": title}}]},
                "이용시간": {"date": {"start": start, "end": end}},
                "용도": {
                    "select": {
                        "name": purpose,
                    }
                },
            },
        }

        data = json.dumps(new_page_data)
        response = requests.post(temp.get("create_page_url"), headers=self.headers, data=data)
        return {"status_code": response.status_code}


def create_reservation(self, database_name=None, room=None, title=None, purpose=None, start=None, end=None):

    database_id = self.get_database_id(database_name)
    create_page_url = self._get_url(type="create_page", database_id=database_id)

    newPageData = {
        "parent": {"database_id": database_id},
        "properties": {
            "방": {
                "select": {
                    "name": room,
                },
            },
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
    response = requests.post(create_page_url, headers=self.headers, data=data)
    return {"status_code": response.status_code}


notion = Notion()
