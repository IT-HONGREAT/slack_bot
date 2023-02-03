class TempBot:
    def __init__(self, temp_name):

        self.action_name = temp_name

    @classmethod
    def get_action(cls):
        # TODO action class name input

        return

    action_settings = {
        "get_reservation": ":one: 테이블링 예약조회",
        "create_reservation": ":two: 테이블 예약생성",
    }

    action_list = [
        {
            "type": "button",
            "text": {"type": "plain_text", "text": value, "emoji": True},
            "action_id": key,
        }
        for key, value in action_settings.items()
    ]
