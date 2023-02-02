from slack_bolt import App

from notion.app import Notion
from slack_mod.app import slack_setting

notion = Notion()
app_1 = App(token=slack_setting.slack_bot_token)


from slack_bolt.async_app import AsyncApp

app = AsyncApp(token=slack_setting.slack_bot_token)
