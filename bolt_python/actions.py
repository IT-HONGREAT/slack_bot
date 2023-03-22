from datetime import datetime
from logging import Logger

from slack_bolt import BoltContext
from slack_sdk import WebClient

from bolt_python.app import bolt_app
from bolt_python.contexts import ANONYMOUS_BOARD_CHANNEL
from bolt_python.forms import modal_form
from bolt_python.utils import validate_reservation, get_random, datetime_to_timestamp, get_user_information
from notion.actions import create_reservation, get_lunch


@bolt_app.message("hello")
def message_hello(message, say, client: WebClient, context: BoltContext, logger: Logger):
    user_info = client.users_info(user=context.user_id)
    email_address = user_info["user"]["profile"]["email"]
    logger.info(email_address)
    say(f"Hey there <@{message['user']}>!")


@bolt_app.shortcut("create_reservation")  # same as slack's callback_id
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
                    placeholder_text="지니/어스",
                    element_option_list=["지니", "어스"],
                    label_text="회의실 선택",
                    block_name="reservation_room",
                ),
                modal_form.select_block(
                    placeholder_text="용도",
                    element_option_list=["일반 회의", "내부 회의", "클라이언트 미팅", "기타"],
                    label_text="회의실 선택",
                    block_name="reservation_purpose",
                ),
                modal_form.date_or_time_block(
                    picker_type="date",
                    placeholder_date_or_time=datetime.now().strftime("%Y-%m-%d"),
                    label_text="예약일",
                    block_name="reservation_date",
                ),
                modal_form.date_or_time_block(
                    picker_type="time",
                    placeholder_date_or_time="09:00",
                    label_text="시작 시간",
                    block_name="reservation_start_time",
                ),
                modal_form.date_or_time_block(
                    picker_type="time",
                    placeholder_date_or_time="19:00",
                    label_text="종료 시간",
                    block_name="reservation_end_time",
                ),
            ],
        },
    )


@bolt_app.view("view_reservation")
def make_reservation(ack, body, client, view, logger):
    ack()
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
    # ack()
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
    ack()
    try:
        picked_food = get_random(food_list)
        say(f"오늘의 랜덤메뉴는 {picked_food['food_name']} 입니다.")

    except Exception as e:
        print("notion lunch table error : ", e)
        say(f"노션 메뉴테이블을 확인해주세요.")


@bolt_app.action("send_dm_anonymous")
def send_dm_anonymous_modal(ack, body, client):
    ack()
    client.views_open(
        trigger_id=body["trigger_id"],
        view={
            "type": "modal",
            "callback_id": "view_dm_anonymous",
            "title": {"type": "plain_text", "text": "마음의 편지"},
            "submit": {"type": "plain_text", "text": "전송하기"},
            "blocks": [
                modal_form.select_user_block(
                    text="수신자",
                    placeholder_text="편지를 보낼 유저를 선택해주세요. 익명이 보장됩니다.",
                    block_name="select_user_dm",
                ),
                modal_form.plain_text_block(
                    text="마음의 편지",
                    placeholder_text="전하고 싶은 말을 적어주세요.",
                    block_name="context_dm",
                    is_multiline=True,
                ),
            ],
        },
    )


@bolt_app.view("view_dm_anonymous")
def send_dm(ack, body, client, view, logger):
    init_value = view["state"]["values"]
    users = init_value["select_user_dm"]["multi_users_select-action"]["selected_users"]
    context_dm = init_value["context_dm"]["plain_text_input-action"]["value"]
    # user = body["user"]["id"]

    errors = {}
    if not init_value:
        errors["values"] = "value error"
    if len(errors) > 0:
        ack(response_action="errors", errors=errors)
        return
    ack()
    try:
        for user in users:
            client.chat_postMessage(channel=user, text=f"익명으로부터 : {context_dm}")
    except Exception as e:
        logger.exception(f"발송실패 {e}")


@bolt_app.action("send_dm_schedule")
def send_dm_anonymous_modal(ack, body, client):
    ack()
    client.views_open(
        trigger_id=body["trigger_id"],
        view={
            "type": "modal",
            "callback_id": "view_dm_schedule",
            "title": {"type": "plain_text", "text": "메세지 예약발송"},
            "submit": {"type": "plain_text", "text": "전송예약하기"},
            "blocks": [
                modal_form.select_user_block(
                    text="수신자",
                    placeholder_text="예약 메세지를 보낼 유저를 선택해주세요. 한번 전송하면 취소할 수 없습니다.",
                    block_name="select_user_dm",
                ),
                modal_form.date_or_time_block(
                    picker_type="date",
                    placeholder_date_or_time=datetime.now().strftime("%Y-%m-%d"),
                    label_text="발송될 날짜",
                    block_name="dm_schedule_date",
                ),
                modal_form.date_or_time_block(
                    picker_type="time",
                    placeholder_date_or_time="09:00",
                    label_text="발송될 시간",
                    block_name="dm_schedule_time",
                ),
                modal_form.plain_text_block(
                    text="예약 메세지",
                    placeholder_text="내용을 입력해주세요. 예약발송 후 수정할 수 없습니다.",
                    block_name="context_dm_schedule",
                    is_multiline=True,
                ),
            ],
        },
    )


@bolt_app.view("view_dm_schedule")
def send_dm(ack, body, client, view, logger):
    user_list = client.users_list()
    init_value = view["state"]["values"]

    users = init_value["select_user_dm"]["multi_users_select-action"]["selected_users"]
    context_dm_schedule = init_value["context_dm_schedule"]["plain_text_input-action"]["value"]
    dm_schedule_date = init_value["dm_schedule_date"]["datepicker-action"]["selected_date"]
    dm_schedule_time = init_value["dm_schedule_time"]["timepicker-action"]["selected_time"]
    sender = body["user"]["id"]
    scheduled_datetime = f"{dm_schedule_date} {dm_schedule_time}"

    errors = {}
    if not init_value:
        errors["values"] = "value error"
    if len(errors) > 0:
        ack(response_action="errors", errors=errors)
        return
    ack()
    try:
        if users:

            user_name_list = []
            for user_id in users:
                scheduled_dm_timestamp = datetime_to_timestamp(f"{dm_schedule_date} {dm_schedule_time}")
                client.chat_scheduleMessage(
                    channel=user_id,
                    post_at=scheduled_dm_timestamp,
                    text=f"{context_dm_schedule}",
                )
                user_name_list.append(get_user_information(user_list, client_user_id=user_id))
            client.chat_postMessage(
                channel=sender,
                text=f"요청하신 예약발송이 정상적으로 등록되었습니다.  예정 발송시간 :{scheduled_datetime} .  대상 : {','.join(user_name_list)}",
            )
        else:
            client.chat_postMessage(channel=sender, text="예약 발송이 정상적으로 등록되지 않았습니다.")

    except Exception as e:
        logger.exception(f"발송실패 {e}")


@bolt_app.action("send_anonymous_board")
def send_anonymous_board_modal(ack, body, client):
    ack()
    client.views_open(
        trigger_id=body["trigger_id"],
        view={
            "type": "modal",
            "callback_id": "view_anonymous_board",
            "title": {"type": "plain_text", "text": "익명 게시판"},
            "submit": {"type": "plain_text", "text": "전송하기"},
            "blocks": [
                modal_form.plain_text_block(
                    text="닉네임",
                    placeholder_text="사용하지 않으려면 비워도 좋습니다.",
                    block_name="nickname_to_anonymous_board",
                    is_multiline=False,
                    optional=True,
                ),
                modal_form.plain_text_block(
                    text="익명이 보장됩니다. 단 서로 배려하는 마음과 예의를 지켜주세요~!",
                    placeholder_text="전하고 싶은 말을 적어주세요.",
                    block_name="context_to_anonymous_board",
                    is_multiline=True,
                ),
            ],
        },
    )


@bolt_app.view("view_anonymous_board")
def send_dm(ack, body, client, view, logger):
    init_value = view["state"]["values"]
    nickname_to_anonymous_board = init_value["nickname_to_anonymous_board"]["plain_text_input-action"]["value"]
    context_to_anonymous_board = init_value["context_to_anonymous_board"]["plain_text_input-action"]["value"]

    errors = {}
    if not init_value:
        errors["values"] = "value error"
    if len(errors) > 0:
        ack(response_action="errors", errors=errors)
        return
    ack()
    try:
        who = ""
        if nickname_to_anonymous_board:
            who = f"{nickname_to_anonymous_board}님의 외침 :"
        client.chat_postMessage(channel=ANONYMOUS_BOARD_CHANNEL, text=f"{who} {context_to_anonymous_board}")
    except Exception as e:
        logger.exception(f"발송실패 {e}")


actions_check = "💻 bolt_python action is called!"  # instead handler.start() | call check
