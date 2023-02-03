context_1 = {
    "title": {"type": "plain_text", "text": "회의실 예약", "emoji": True},
    "submit": {"type": "plain_text", "text": "예약하기", "emoji": True},
    "type": "modal",
    "close": {"type": "plain_text", "text": "취소", "emoji": True},
    "blocks": [
        {
            "type": "input",
            "element": {
                "type": "static_select",
                "placeholder": {"type": "plain_text", "text": "지니/어스", "emoji": True},
                "options": [
                    {"text": {"type": "plain_text", "text": "지니", "emoji": True}, "value": "value-0"},
                    {"text": {"type": "plain_text", "text": "어스", "emoji": True}, "value": "value-1"},
                ],
                "action_id": "static_select-action",
            },
            "label": {"type": "plain_text", "text": "회의실 선택", "emoji": True},
        },
        {
            "type": "input",
            "element": {
                "type": "datepicker",
                "initial_date": "2023-01-01",
                "placeholder": {"type": "plain_text", "text": "예약일", "emoji": True},
                "action_id": "datepicker-action",
            },
            "label": {"type": "plain_text", "text": "예약일", "emoji": True},
        },
        {
            "type": "input",
            "element": {
                "type": "timepicker",
                "initial_time": "10:00",
                "placeholder": {"type": "plain_text", "text": "Select time", "emoji": True},
                "action_id": "timepicker-action",
            },
            "label": {"type": "plain_text", "text": "시작시간", "emoji": True},
        },
        {
            "type": "input",
            "element": {
                "type": "timepicker",
                "initial_time": "19:00",
                "placeholder": {"type": "plain_text", "text": "Select time", "emoji": True},
                "action_id": "timepicker-action",
            },
            "label": {"type": "plain_text", "text": "종료시간", "emoji": True},
        },
    ],
}
