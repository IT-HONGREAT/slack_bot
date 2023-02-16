from urllib.parse import urlparse

from notion.actions import get_reservation_db


def is_time_overlapping(a_start, a_end, b_start, b_end):
    # a 기존시간, b 신청시간
    ttt = False
    if (a_start <= b_start <= a_end) or (a_start <= b_end <= a_end):
        ttt = True
    return ttt


def validate_reservation(data=None, payload=None):
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
