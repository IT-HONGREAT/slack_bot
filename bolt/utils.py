from random import randint
from typing import Optional
from urllib.parse import urlparse

from notion.actions import get_reservation_db


def is_time_overlapping(a_start, a_end, b_start, b_end):  # TODO : 에러 종류 판단 시 return data 변경가능
    # a 기존시간, b 신청시간
    ttt = False
    if (a_start <= b_start <= a_end) or (a_start <= b_end <= a_end):
        ttt = True
    return ttt


def validate_reservation(data: dict, payload: Optional[dict]) -> bool:
    condition = True
    filtered_data = get_reservation_db(
        database_name="reservation",
        payload=payload,
    )
    for one_reservation in filtered_data:
        check_time_overlap = is_time_overlapping(
            one_reservation["start"],
            one_reservation["end"],
            data["reservation_start_time"],
            data["reservation_end_time"],
        )

        if check_time_overlap:
            if data["reservation_purpose"] == "클라이언트 미팅":
                if one_reservation["tag"] == "클라이언트 미팅":
                    condition = False

            if data["reservation_purpose"] != "클라이언트 미팅":
                condition = False
    return condition


def check_direct_link(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def make_button_blocks(dictionary):

    dict_to_list = [
        {
            "type": "button",
            "text": {"type": "plain_text", "text": description, "emoji": True},
            "url": some_value,
        }
        if check_direct_link(some_value)
        else {
            "type": "button",
            "text": {"type": "plain_text", "text": description, "emoji": True},
            "action_id": some_value,
        }
        for some_value, description in dictionary.items()
    ]
    return dict_to_list


def get_random(some_list):
    return some_list[randint(0, len(some_list) - 1)]


def get_user_id(slack_users, user_email=None):
    user_id = ""
    user_information = {}
    members = slack_users.get("members")
    for one_member in members:
        user_id = one_member["id"]
        profile = one_member.get("profile")
        if profile:
            email = one_member.get("profile").get("email")
            if email:
                user_information[email] = user_id
    return user_information.get(user_email)
