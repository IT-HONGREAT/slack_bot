from settings import PlatFormSetting


class Slack(PlatFormSetting):
    def __init__(self):
        """
        If you need to add some token or secret_key for [slack or bolt] setup, add it here.

        If there is a better way, please suggest to in-yeong.
        """
        super().__init__()
        self.slack_bot_token = self.get_slack_detail_key("bot_token")
        self.slack_app_token = self.get_slack_detail_key("app_token")


slack_setting = Slack()
