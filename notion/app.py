from typing import Optional

import requests

from settings import PlatformSetting


class Notion(PlatformSetting):
    # Add some notion settings here.
    def __init__(self):
        super().__init__()
        try:
            self.headers = {
                "Authorization": "Bearer " + self.token,
                "accept": "application/json",
                "Notion-Version": "2022-06-28",
                "content-type": "application/json",
            }
        except TypeError as e:
            print("notion token for header : ", e)

    def _get_url(self, type: Optional[str] = "read_db", database_id=None):
        """
        :param type: read/create ex) "read"
        :param database_id:
        :return: url ex)https://~~~
        """

        # Add url notion CRUD or others here.
        url_for_function = {
            "read_db": f"https://api.notion.com/v1/databases/{database_id}/query",
            "create_page": "https://api.notion.com/v1/pages",
        }

        return url_for_function.get(type)

    # TODO get_db_result instead get_db ???
    def get_db(self, database_name=None):

        read_url = self._get_url(type="read_db", database_id=self.get_database_id(database_name))

        response = requests.post(read_url, headers=self.headers)
        data = response.json()
        data_result = data.get("results")

        for i in data_result:
            print("<your data_result> ")

        return {"status_code": data.status_code}

    def get_db_result(self, database_name=None, payload=None):
        read_url = self._get_url(type="read_db", database_id=self.get_database_id(database_name))
        data_result = ""
        try:
            response = requests.post(read_url, headers=self.headers, json=payload)
            data = response.json()
            data_result = data.get("results")

        except AttributeError as e:
            print("notion request URL is something wrong :", e)

        return data_result

    def create_page(self, database_name=None):
        database_id = self.get_database_id(database_name)
        create_page_url = self._get_url(type="create_page", database_id=database_id)

        return {
            "database_id": database_id,
            "create_page_url": create_page_url,
        }


notion = Notion()
