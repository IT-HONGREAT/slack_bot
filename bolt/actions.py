from slack_bolt.adapter.socket_mode import SocketModeHandler

from bolt.app import slack_setting
from bolt.main import app
from notion.app import notion


@app.message("hello")
async def message_hello(message, say):

    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Hey there <@{message['user']}>!"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Click Me"},
                    "action_id": "button_click",
                },
            }
        ],
        text=f"Hey there <@{message['user']}>!",
    )


# 분기
# action_settings = {
#     "get_reservation": ":one: 테이블링 예약조회",
#     "create_reservation": ":two: 테이블 예약생성",
# }
#
#
# action_list = [
#     {
#         "type": "button",
#         "text": {"type": "plain_text", "text": value, "emoji": True},
#         "action_id": key,
#     }
#     for key, value in action_settings.items()
# ]
#
#
# @app.message("bot")
# def message_bot(message, say):
#     say(
#         blocks=[
#             {
#                 "type": "section",
#                 "text": {
#                     "type": "mrkdwn",
#                     "text": "*똑봇 테스트*\n 아아 테스트 중입니다. <http://naver.com|네이버 메인!>.",
#                 },
#             },
#             {"type": "context", "elements": [{"type": "mrkdwn", "text": "<http://kakao.com|ㅋㅋㅋㅋ>"}]},
#             {
#                 "type": "actions",
#                 "elements": action_list,
#             },
#         ],
#     )


@app.action("get_reservation")
def action_button_click(body, ack, say):
    ack()
    link = "https://www.notion.so/486b0c639daf40d89ba2538e7214e47f?v=e37566dd51e646c19291259ed17b4157"
    say(f"<@{body['user']['id']}> clicked the button,,,,{link}")


# temp = [
#     {
#         "type": "input",
#         "element": {
#             "type": "static_select",
#             "placeholder": {"type": "plain_text", "text": "지니/어스", "emoji": True},
#             "options": [
#                 {"text": {"type": "plain_text", "text": "지니", "emoji": True}, "value": "value-0"},
#                 {"text": {"type": "plain_text", "text": "어스", "emoji": True}, "value": "value-1"},
#             ],
#             "action_id": "static_select-action",
#         },
#         "label": {"type": "plain_text", "text": "회의실 선택", "emoji": True},
#     },
#     {
#         "type": "input",
#         "element": {
#             "type": "datepicker",
#             "initial_date": "2023-01-01",
#             "placeholder": {"type": "plain_text", "text": "예약일", "emoji": True},
#             "action_id": "datepicker-action",
#         },
#         "label": {"type": "plain_text", "text": "예약일", "emoji": True},
#     },
#     {
#         "type": "input",
#         "element": {
#             "type": "timepicker",
#             "initial_time": "10:00",
#             "placeholder": {"type": "plain_text", "text": "Select time", "emoji": True},
#             "action_id": "timepicker-action",
#         },
#         "label": {"type": "plain_text", "text": "시작시간", "emoji": True},
#     },
#     {
#         "type": "input",
#         "element": {
#             "type": "timepicker",
#             "initial_time": "19:00",
#             "placeholder": {"type": "plain_text", "text": "Select time", "emoji": True},
#             "action_id": "timepicker-action",
#         },
#         "label": {"type": "plain_text", "text": "종료시간", "emoji": True},
#     },
# ]
temp = {
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


# temp = {
#     "title": {"type": "plain_text", "text": "Modal Title"},
#     "submit": {"type": "plain_text", "text": "Submit"},
#     "blocks": [
#         {
#             "type": "input",
#             "block_id": "edit-task-title",
#             "label": {"type": "plain_text", "text": "Task title"},
#             "element": {
#                 "type": "plain_text_input",
#                 "action_id": "task-title-value",
#                 "initial_value": "Block Kit documentation",
#             },
#         },
#         {
#             "type": "input",
#             "block_id": "edit-ticket-desc",
#             "label": {"type": "plain_text", "text": "Ticket description"},
#             "element": {
#                 "type": "plain_text_input",
#                 "multiline": True,
#                 "action_id": "ticket-desc-value",
#                 "initial_value": "Update Block Kit documentation to include Block Kit in new surface areas (like modals).",
#             },
#         },
#     ],
#     "type": "modal",
# }


# 임시저장

# # TODO 분기


@app.action("create_reservation")
def action_button_click(body, ack, say):
    ack()

    notion.create_reservation(
        database_name="reservation",
        room="어스",
        title="팀 회의 등록",
        purpose="내부회의",
        start="2023-02-01T01:00:00",
        end="2023-02-02T16:00:00",
    )
    say(
        **temp,
    )


bolt_socket = SocketModeHandler(app, slack_setting.slack_app_token).start()
