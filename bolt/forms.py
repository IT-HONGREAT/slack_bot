class BlockForm:  # TODO or make contextform

    """
    make(like get) block format for view

    select_block => static_select
    date_or_time_block => datepicker or timepicker

    ...add any field.
    """

    def select_block(
        self,
        element_type: str,
        placeholder_text: str | None,
        element_option_list: list,
        label_text: str,
        block_name: str,
    ) -> dict:

        """
        element_option_list = ["선택1","선택2","선택3"]
        """

        options_form = [
            {"text": {"type": "plain_text", "text": comp, "emoji": True}, "value": f"value-{idx}"}
            for idx, comp in enumerate(element_option_list)
        ]

        context = {
            "type": "input",
            "element": {
                "type": element_type,
                "placeholder": {"type": "plain_text", "text": placeholder_text, "emoji": True},
                "options": options_form,
                "action_id": f"{element_type}-action",
            },
            "label": {"type": "plain_text", "text": label_text, "emoji": True},
            "block_id": block_name,
        }

        return context

    def date_or_time_block(
        self,
        element_type: str,
        placeholder_date_or_time: str | None,
        label_text: str,
        block_name: str,
    ) -> dict:

        """
        if element_type is datepicker
            placeholder_date_or_time = "2023-01-01"
        if element_type is datepicker
            placeholder_date_or_time = "10:00"
        """
        date_or_time = element_type[:4]

        context = {
            "type": "input",
            "element": {
                "type": element_type,
                f"initial_{date_or_time}": placeholder_date_or_time,
                "action_id": f"{element_type}-action",
            },
            "label": {"type": "plain_text", "text": label_text, "emoji": True},
            "block_id": block_name,
        }

        return context

    def plain_text_block(
        self,
        element_type: str,
        text: str,
        placeholder_text: str,
        block_name: str,
        is_multiline: bool,
    ) -> dict:

        context = {
            "type": "input",
            "element": {
                "type": element_type,
                "multiline": is_multiline,
                "action_id": f"{element_type}-action",
                "placeholder": {"type": "plain_text", "text": placeholder_text, "emoji": True},
            },
            "label": {
                "type": "plain_text",
                "text": text,
                "emoji": True,
            },
            "block_id": block_name,
        }

        return context

    def select_user_block(
        self,
        text: str,
        placeholder_text: str,
        block_name: str,
    ) -> dict:

        context = {
            "type": "input",
            "element": {
                "type": "multi_users_select",
                "placeholder": {"type": "plain_text", "text": placeholder_text, "emoji": True},
                "action_id": "multi_users_select-action",
            },
            "label": {"type": "plain_text", "text": text, "emoji": True},
            "block_id": block_name,
        }

        return context


modal_form = BlockForm()  # TODO 사용성 개선
