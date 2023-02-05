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
