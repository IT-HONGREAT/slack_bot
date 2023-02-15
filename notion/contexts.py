import datetime


def create_new_properity(username, exercise_count_dict):
    new_property = {
        "운동": {
            "rich_text": [
                {
                    "annotations": {
                        "bold": False,
                        "code": False,
                        "color": "default",
                        "italic": False,
                        "strikethrough": False,
                        "underline": False,
                    },
                    "href": None,
                    "plain_text": exercise_count_dict,
                    "text": {
                        "content": exercise_count_dict,
                        "link": None,
                    },
                    "type": "text"}
            ],
            "type": "rich_text",
        },
        "이름": {
            "id": "title",
            "title": [
                {
                    "annotations": {
                        "bold": False,
                        "code": False,
                        "color": "default",
                        "italic": False,
                        "strikethrough": False,
                        "underline": False,
                    },
                    "href": None,
                    "plain_text": username,
                    "text": {"content": username, "link": None},
                    "type": "text",
                },
            ],
            "type": "title",
        },
        "날짜": {
            "rich_text": [
                {
                    "annotations": {
                        "bold": False,
                        "code": False,
                        "color": "default",
                        "italic": False,
                        "strikethrough": False,
                        "underline": False,
                    },
                    "href": None,
                    "plain_text": datetime.datetime.now().strftime("%Y / %m / %d"),
                    "text": {
                        "content": datetime.datetime.now().strftime("%Y / %m / %d"),
                        "link": None,
                    },
                    "type": "text"}
            ],
            "type": "rich_text",
        },
    }

    return new_property
