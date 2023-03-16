from bolt_python.app import bolt_app, slack_setting


# Call main bot buttons


@bolt_app.event("app_mention")
def handle_app_mention(message: dict, say: callable) -> None:
    """
    Handles @mention event in Slack
    """
    say(
        blocks=[
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": ":information_desk_person: slack bot",
                    "emoji": True,
                },
            },
            {"type": "context", "elements": [{"type": "mrkdwn", "text": "<http://naver.com|ex-naver link>"}]},
            {
                "type": "actions",
                "elements": slack_setting.function_button,
            },
        ],
    )


main_button_check = "🧑🏻‍💻 bolt_python main button is called!"  # instead handler | call check
