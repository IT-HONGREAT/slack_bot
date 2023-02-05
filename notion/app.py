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

        # Add url notion CRUD or others here.
        url_for_function = {
            "read_db": f"https://api.notion.com/v1/databases/{database_id}/query",
            "create_page": "https://api.notion.com/v1/pages",
        }

        return url_for_function.get(type)

    def get_db(self, database_name=None):

        read_url = self._get_url(type="read_db", database_id=self.get_database_id(database_name))

        response = requests.post(read_url, headers=self.headers)
        data = response.json()
        data_result = data.get("results")

        for i in data_result:
            print("<your data_result> ")

        return {"status_code": data.status_code}

    def create_page(self, database_name=None):
        database_id = self.get_database_id(database_name)
        create_page_url = self._get_url(type="create_page", database_id=database_id)

        return {
            "database_id": database_id,
            "create_page_url": create_page_url,
        }


notion = Notion()
