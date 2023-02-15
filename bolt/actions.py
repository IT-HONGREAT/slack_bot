from datetime import timezone, datetime

from bolt.contexts import context_example, ohunwan_block, excercise_input
from bolt.main import app, Handler
from bolt.forms import modal_form
from bolt.utils import validate_reservation
from notion.actions import example_action_function, create_reservation, get_reservation_db, create_ohunwan


@app.message("hello")
def message_hello(message, say):
    say(text=f"Hey there <@{message['user']}>!")


@app.action("get_reservation")
def get_reservation(body, ack, say):
    ack()
    say(context_example)


@app.action("create_reservation")
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


@app.view("view_reservation")
def make_reservation(ack, body, client, view, logger):

    reservation_modal_values = view["state"]["values"]

    reservation_room = reservation_modal_values["reservation_room"]["static_select-action"]["selected_option"]["text"][
        "text"
    ]
    reservation_purpose = reservation_modal_values["reservation_purpose"]["static_select-action"]["selected_option"][
        "text"
    ]["text"]
    reservation_date = reservation_modal_values["reservation_date"]["datepicker-action"]["selected_date"]
    reservation_start_time = reservation_modal_values["reservation_start_time"]["timepicker-action"]["selected_time"]
    reservation_end_time = reservation_modal_values["reservation_end_time"]["timepicker-action"]["selected_time"]

    # TODO fix naming + pipeline function
    temp_data = dict(
        reservation_start_time=reservation_start_time,
        reservation_end_time=reservation_end_time,
        reservation_purpose=reservation_purpose,
    )

    reservation_condition = validate_reservation(
        data=temp_data,
        payload={
            "filter": {
                "and": [
                    {
                        "property": "이용시간",
                        "date": {"equals": reservation_date},
                    },
                    {
                        "property": "방",
                        "select": {"equals": reservation_room},
                    },
                ]
            }
        },
    )

    if reservation_condition:
        # notion insert
        create_reservation(
            database_name="reservation",
            room=reservation_room,
            title="팀 회의 등록",
            purpose=reservation_purpose,
            start=f"{reservation_date}T{reservation_start_time}:00",
            end=f"{reservation_date}T{reservation_end_time}:00",
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


@app.action("get_ohunwan_block")
def get_ohunwan_block(ack, say):
    ack()
    say(
        blocks=ohunwan_block,
        text="오운완",
    )


@app.action("get_exercise_input")
def get_exercise_input(ack, client, body):
    ack()

    ohunwan_block.insert(-1, excercise_input)

    client.chat_update(
        channel=body["channel"]["id"],
        ts=body["message"]["ts"],
        blocks=ohunwan_block,
        as_user=True,
    )


@app.action("create_ohunwan_notion")
def create_ohunwan_notion(ack, body, say):
    ack()

    username = body["user"]["name"]
    exercise_count_dict = {}
    error_cnt = 0

    if body["state"]["values"]:
        for value_info in body["state"]["values"].items():
            value = value_info[1]["plain_text_input-action"]["value"]

            if value is not None:
                exercise_count_dict[value.split(" ")[0]] = value.split(" ")[1]
            else:
                error_cnt += 1

        if error_cnt >= 1:
            say("`운동이름 횟수(시간)`을 입력해주세요!")
        else:
            create_ohunwan(database_name="오운완", username=username, exercise_count_dict=str(exercise_count_dict))
            say("`노션`에 입력하신 운동정보가 등록되었습니다! `노션에서 확인`해주세요!")
    else:
        say("`운동이름 횟수(시간)`을 입력해주세요!")


bolt_socket = Handler.start()
