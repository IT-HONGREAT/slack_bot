class BlockForm:  # TODO or make contextform

    """
    make(like get) block format for view

    select_block => static_select
    date_or_time_block => datepicker or timepicker

    ...add any field.


    BlockForm.
    """

    def __init__(self):
        self.input_block = {
            "type": "input",
            "element": {},
            "label": {},
            "block_id": "<your-block_name-for-block_id>",
        }

    def select_block(
        self,
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
            **self.input_block,
            **{
                "element": {
                    "type": "static_select",
                    "placeholder": {"type": "plain_text", "text": placeholder_text, "emoji": True},
                    "options": options_form,
                    "action_id": "static_select-action",
                },
                "label": {"type": "plain_text", "text": label_text, "emoji": True},
                "block_id": block_name,
            },
        }

        return context

    def date_or_time_block(
        self,
        picker_type: str,
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
        date_or_time = picker_type
        # date_or_time = element_type[:4]
        context = {
            **self.input_block,
            **{
                "element": {
                    "type": f"{date_or_time}picker",
                    f"initial_{date_or_time}": placeholder_date_or_time,
                    "action_id": f"{date_or_time}picker-action",
                },
                "label": {"type": "plain_text", "text": label_text, "emoji": True},
                "block_id": block_name,
            },
        }

        return context

    def plain_text_block(
        self,
        text: str,
        placeholder_text: str,
        block_name: str,
        is_multiline: bool,
    ) -> dict:
        context = {
            **self.input_block,
            **{
                "element": {
                    "type": "plain_text_input",
                    "multiline": is_multiline,
                    "action_id": "plain_text_input-action",
                    "placeholder": {"type": "plain_text", "text": placeholder_text, "emoji": True},
                },
                "label": {
                    "type": "plain_text",
                    "text": text,
                    "emoji": True,
                },
                "block_id": block_name,
            },
        }

        return context

    def select_user_block(
        self,
        text: str,
        placeholder_text: str,
        block_name: str,
    ) -> dict:
        context = {
            **self.input_block,
            **{
                "element": {
                    "type": "multi_users_select",
                    "placeholder": {"type": "plain_text", "text": placeholder_text, "emoji": True},
                    "action_id": "multi_users_select-action",
                },
                "label": {"type": "plain_text", "text": text, "emoji": True},
                "block_id": block_name,
            },
        }

        return context


modal_form = BlockForm()
