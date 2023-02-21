from datetime import datetime
from logging import Logger

from slack_bolt import BoltContext
from slack_sdk import WebClient

from bolt.app import bolt_app
from bolt.forms import modal_form
from bolt.main import bolt_socket_handler
from bolt.utils import validate_reservation, get_random
from notion.actions import create_reservation, get_lunch


@bolt_app.message("hello")
def message_hello(message, say, client: WebClient, context: BoltContext, logger: Logger):
    user_info = client.users_info(user=context.user_id)
    email_address = user_info["user"]["profile"]["email"]
    logger.info(email_address)
    say(f"Hey there <@{message['user']}>!")


@bolt_app.action("create_reservation")
def create_reservation_modal(ack, body, client):
    ack()
    client.views_open(
        trigger_id=body["trigger_id"],
        view={
            "type": "modal",
            "callback_id": "view_reservation",
            "title": {"type": "plain_text", "text": "회의실 예약"},
            "submit": {"type": "plain_text", "text": "예약하기"},
            "blocks": [
                modal_form.select_block(
                    element_type="static_select",
                    placeholder_text="지니/어스",
                    element_option_list=["지니", "어스"],
                    label_text="회의실 선택",
                    block_name="reservation_room",
                ),
                modal_form.select_block(
                    element_type="static_select",
                    placeholder_text="용도",
                    element_option_list=["일반 회의", "내부 회의", "클라이언트 미팅", "기타"],
                    label_text="회의실 선택",
                    block_name="reservation_purpose",
                ),
                modal_form.date_or_time_block(
                    element_type="datepicker",
                    placeholder_date_or_time=datetime.now().strftime("%Y-%m-%d"),
                    label_text="예약일",
                    block_name="reservation_date",
                ),
                modal_form.date_or_time_block(
                    element_type="timepicker",
                    placeholder_date_or_time="09:00",
                    label_text="시작 시간",
                    block_name="reservation_start_time",
                ),
                modal_form.date_or_time_block(
                    element_type="timepicker",
                    placeholder_date_or_time="19:00",
                    label_text="종료 시간",
                    block_name="reservation_end_time",
                ),
            ],
        },
    )


@bolt_app.view("view_reservation")
def make_reservation(ack, body, client, view, logger):
    reservation_modal_values = view["state"]["values"]
    reservation_mapper = {
        "reservation_modal_values": view["state"]["values"],
        "reservation_room": reservation_modal_values["reservation_room"]["static_select-action"]["selected_option"][
            "text"
        ]["text"],
        "reservation_purpose": reservation_modal_values["reservation_purpose"]["static_select-action"][
            "selected_option"
        ]["text"]["text"],
        "reservation_date": reservation_modal_values["reservation_date"]["datepicker-action"]["selected_date"],
        "reservation_start_time": reservation_modal_values["reservation_start_time"]["timepicker-action"][
            "selected_time"
        ],
        "reservation_end_time": reservation_modal_values["reservation_end_time"]["timepicker-action"]["selected_time"],
    }

    reservation_condition = validate_reservation(
        data=reservation_mapper,
        payload={
            "filter": {
                "and": [
                    {
                        "property": "이용시간",
                        "date": {"equals": reservation_mapper["reservation_date"]},
                    },
                    {
                        "property": "방",
                        "select": {"equals": reservation_mapper["reservation_room"]},
                    },
                ]
            }
        },
    )

    if reservation_condition:
        # notion insert
        create_reservation(
            database_name="reservation",
            room=reservation_mapper["reservation_room"],
            title="팀 회의 등록",
            purpose=reservation_mapper["reservation_purpose"],
            start=f"{reservation_mapper['reservation_date']}T{reservation_mapper['reservation_start_time']}:00",
            end=f"{reservation_mapper['reservation_date']}T{reservation_mapper['reservation_end_time']}:00",
        )

    init_value = view["state"]["values"]
    user = body["user"]["id"]
    errors = {}
    if not init_value:
        errors["values"] = "value error"
    if len(errors) > 0:
        ack(response_action="errors", errors=errors)
        return
    ack()
    msg = ""
    try:
        msg = f"요청한 시간에 회의실이 예약되었습니다."
        if not reservation_condition:
            msg = "요청한 시간에 예약할 수 없습니다."
    except Exception as e:
        msg = "제출관련 에러가 발생했습니다. 개발자에게 문의 해주세요."

    try:
        client.chat_postMessage(channel=user, text=msg)
    except e:
        logger.exception(f"발송실패 {e}")


@bolt_app.action("get_lunch_menu")
def get_lunch_menu(body, ack, say):
    food_list = get_lunch(database_name="lunch")
    picked_food = get_random(food_list)
    ack()
    say(f"오늘의 랜덤메뉴는 {picked_food['food_name']} 입니다.")


bolt_socket = bolt_socket_handler.start()
