# import json
# from typing import Optional
#
# import aiohttp
# import requests
#
# from settings import PlatFormSetting
#
#
# class Notion(PlatFormSetting):
#     # Add some notion settings here.
#     def __init__(self):
#         super().__init__()
#         self.headers = {
#             "Authorization": "Bearer " + self.token,
#             "accept": "application/json",
#             "Notion-Version": "2022-06-28",
#             "content-type": "application/json",
#         }
#
#     async def fetch_data(self, url: str, headers: str):
#         async with aiohttp.ClientSession() as session:
#             async with session.get(url, headers=headers) as response:
#                 return await response.json()
#
#     def _get_url(self, type: Optional[str] = "read_db", database_id=None):
#         """
#         :param type: read/create ex) "read"
#         :param database_id:
#         :return: url ex)https://~~~
#         """
#
#         temp_mapping = {
#             "read_db": f"https://api.notion.com/v1/databases/{database_id}/query",
#             "create_page": "https://api.notion.com/v1/pages",
#         }
#
#         return temp_mapping.get(type)
#
#     # TODO read, create 함수 분기
#
#     async def get_reservation(self, database_name=None):
#
#         read_url = self._get_url(type="read_db", database_id=self.get_database_id(database_name))
#
#         """동기"""
#         # response = requests.post(read_url, headers=self.headers)
#         # data = response.json()
#         # data_result = data.get("results")
#
#         """비동기"""
#         data = self.fetch_data(read_url, self.headers)
#
#         data_result = data["results"]
#
#         for i in data_result:
#             one_property = i.get("properties")
#
#             room = one_property["방"]["select"]["name"]
#             created_by = one_property["생성자"]["created_by"]["name"]
#             title = one_property["제목"]["title"][0].get("plain_text")
#             time = one_property["이용시간"].get("date")
#             if time:
#                 start = time.get("start")
#                 end = time.get("end")
#             tag = one_property["용도"]["select"]["name"]
#
#             print("방", "=>", room)
#             print("생성자", "=>", created_by)
#             print("제목", "=>", title)
#             if time:
#                 print("이용시간", "=>", start)
#                 print("이용시간", "=>", end)
#             print("용도", "=>", tag)
#
#         return {"status_code": data.status_code}
#
#     # TODO read, create 함수 분기
#     def create_reservation(self, database_name=None, room=None, title=None, purpose=None, start=None, end=None):
#
#         database_id = self.get_database_id(database_name)
#         create_page_url = self._get_url(type="create_page", database_id=database_id)
#
#         newPageData = {
#             "parent": {"database_id": database_id},
#             "properties": {
#                 "방": {
#                     "select": {
#                         "name": room,
#                     },
#                 },
#                 "제목": {"title": [{"text": {"content": title}}]},
#                 "이용시간": {"date": {"start": start, "end": end}},
#                 "용도": {
#                     "select": {
#                         "name": purpose,
#                     }
#                 },
#             },
#         }
#
#         data = json.dumps(newPageData)
#         response = requests.post(create_page_url, headers=self.headers, data=data)
#         return {"status_code": response.status_code}
#
#
# notion = Notion()
