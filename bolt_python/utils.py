from datetime import datetime
from random import randint
from typing import Optional

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


def get_random(some_list):
    value = ""
    try:
        value = some_list[randint(0, len(some_list) - 1)]
    except Exception as e:
        print("util error : ", e)
    return value


def get_user_information(client_users_list, client_user_email=None, client_user_id=None):
    user_information = {}
    information = ""
    members = client_users_list.get("members")
    for one_member in members:
        user_id = one_member["id"]
        profile = one_member.get("profile")
        if profile:
            email = profile.get("email")
            display_name = profile.get("display_name")
            real_name = profile.get("real_name")
            if client_user_email:
                user_information[email] = user_id
                information = user_information.get(client_user_email)
            if client_user_id:
                user_information[user_id] = {"email": email, "real_name": real_name, "display_name": display_name}
                check = user_information.get(client_user_id)
                if check:
                    information = check.get("display_name")

    return information


def datetime_to_timestamp(date_time: str):  # 2023-03-01 10:10

    datetime_to_float = None
    try:
        datetime_data = datetime.strptime(date_time, "%Y-%m-%d %H:%M")
        datetime_to_float = datetime_data.timestamp()

    except Exception as e:
        print("datetime error : ", e)

    return datetime_to_float
