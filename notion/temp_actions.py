import json

import requests

from notion.temp_refactory_app import notion


def temp_dired_action_function(
    database_name=None,
    room=None,
    title=None,
    start=None,
    end=None,
    purpose=None,
):
    db_info = notion.create_page(database_name=database_name)

    new_page_data = {
        "parent": {"database_id": db_info.get("database_id")},
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
    print("생성확인!!")
    data = json.dumps(new_page_data)
    print("데이터 확인!!", data)
    response = requests.post(db_info.get("create_page_url"), headers=notion.headers, data=data)
    print("post 확인!", response)
    return {"status_code": response.status_code}
