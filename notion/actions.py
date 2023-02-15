import json

import requests

from notion.app import notion


def example_action_function(database_name=None, *args, **kwargs):
    db_info = notion.create_page(database_name=database_name)

    new_page_data = {
        "parent": {"database_id": db_info.get("database_id")},
        "properties": "<your-data-format>",
    }
    data = json.dumps(new_page_data)
    response = requests.post(db_info.get("create_page_url"), headers=notion.headers, data=data)
    return {"status_code": response.status_code}  # You can change anything.


def get_reservation_db(database_name=None, payload=None):

    data_result = notion.get_db_result(database_name=database_name, payload=payload)
    data_reformat_list = []
    if data_result:

        for i in data_result:
            one_property = i.get("properties")
            one_form = {}
            one_form["room"] = one_property["방"]["select"]["name"]
            one_form["created_by"] = one_property["생성자"]["created_by"]["name"]
            one_form["title"] = one_property["제목"]["title"][0].get("plain_text")
            one_form["time"] = one_property["이용시간"].get("date")
            if one_form["time"]:
                one_form["start"] = one_form["time"].get("start").split("T")[1][:5]
                one_form["end"] = one_form["time"].get("end").split("T")[1][:5]
            one_form["tag"] = one_property["용도"]["select"]["name"]

            data_reformat_list.append(one_form)

    return data_reformat_list


def create_reservation(database_name=None, *args, **kwargs):
    db_info = notion.create_page(database_name=database_name)

    new_page_data = {
        "parent": {"database_id": db_info.get("database_id")},
        "properties": {
            "방": {
                "select": {
                    "name": kwargs["room"],
                },
            },
            "제목": {"title": [{"text": {"content": kwargs["title"]}}]},
            "이용시간": {"date": {"start": kwargs["start"], "end": kwargs["end"]}},
            "용도": {
                "select": {
                    "name": kwargs["purpose"],
                }
            },
        },
    }
    data = json.dumps(new_page_data)
    response = requests.post(db_info.get("create_page_url"), headers=notion.headers, data=data)
    return {"status_code": response.status_code}  # You can change anything.
