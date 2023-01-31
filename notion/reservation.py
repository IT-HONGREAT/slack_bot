import requests, json

from envs import get_env


class PlatForm:
    def __init__(self, token=None):
        self.token = token


class Notion(PlatForm):
    def __init__(self, notion_db_name):
        super().__init__()

        # self.db_name = get_env().get(f"{notion_db_name}")
        # self.Notion = get_env().get("Notion")

        self.headers = {
            "Authorization": "Bearer " + self.Notion,
            "accept": "application/json",
            "Notion-Version": "2022-06-28",
            "content-type": "application/json",
        }

    def request_url(self):

        return

    def get_reservation(databaseId, headers):
        readUrl = f"https://api.notion.com/v1/databases/{databaseId}/query"

        response = requests.post(readUrl, headers=headers)
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
