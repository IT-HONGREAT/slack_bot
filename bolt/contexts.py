context_example = f"<@> some text or form(dict)"

ohunwan_block = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "오운완",
            "emoji": True,
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":tada: `운동이름 횟수(시간)` 양식으로 입력해주세요! :tada: \n",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "버튼을 눌러 운동을 추가해주세요! :arrow_right:",
        },
        "accessory": {
            "type": "button",
            "text": {
                "type": "plain_text",
                "text": "운동 추가",
                "emoji": True,
            },
            "value": "click_me_123",
            "action_id": "get_exercise_input",
        },
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": " ",
        },
        "accessory": {
            "type": "button",
            "text": {
                "type": "plain_text",
                "text": "등록",
                "emoji": True,
            },
            "value": "click_me_123",
            "action_id": "create_ohunwan_notion",
        },
    },
]

excercise_input = {
        "type": "input",
        "element": {
            "type": "plain_text_input",
            "action_id": "plain_text_input-action",
        },
        "label": {
            "type": "plain_text",
            "text": " ",
            "emoji": True,
        }
    }