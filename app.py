from fastapi import FastAPI
from slack_bolt.adapter.asgi import SlackRequestHandler

from api_models.temp_model import Alarm
from bolt.app import bolt_app
from bolt.utils import get_user_id

api = FastAPI()
app_handler = SlackRequestHandler(bolt_app)


@api.post("/alarm")
async def alarm(alarm: Alarm):

    # bolt_app.client.chat_postMessage(channel="U04LZ5K7ML2", text=f"{alarm.user_name}님이 {alarm.context}관련 내용을 입력했습니다.")
    # check = bolt_app.client.users_profile_get(include_labels="hongreat95@gmail.com")
    check = bolt_app.client.users_list()
    user_id = get_user_id(check, "hongreat95@gmail.com")

    return {"user_id": user_id}


#
# @api.post("/some_test")
# async def some_logic(req: Request):
#     print("testtesttes!!")
#     # return await app_handler.handle(req)


# uvicorn app:api --reload --port 3000 --log-level warning


check = {
    "ok": True,
    "members": [
        {
            "id": "USLACKBOT",
            "team_id": "T04LZ247MCK",
            "name": "slackbot",
            "deleted": False,
            "color": "757575",
            "real_name": "Slackbot",
            "tz": "America/Los_Angeles",
            "tz_label": "Pacific Standard Time",
            "tz_offset": -28800,
            "profile": {
                "title": "",
                "phone": "",
                "skype": "",
                "real_name": "Slackbot",
                "real_name_normalized": "Slackbot",
                "display_name": "Slackbot",
                "display_name_normalized": "Slackbot",
                "fields": {},
                "status_text": "",
                "status_emoji": "",
                "status_emoji_display_info": [],
                "status_expiration": 0,
                "avatar_hash": "sv41d8cd98f0",
                "always_active": True,
                "first_name": "slackbot",
                "last_name": "",
                "image_24": "https://a.slack-edge.com/80588/img/slackbot_24.png",
                "image_32": "https://a.slack-edge.com/80588/img/slackbot_32.png",
                "image_48": "https://a.slack-edge.com/80588/img/slackbot_48.png",
                "image_72": "https://a.slack-edge.com/80588/img/slackbot_72.png",
                "image_192": "https://a.slack-edge.com/80588/marketing/img/avatars/slackbot/avatar-slackbot.png",
                "image_512": "https://a.slack-edge.com/80588/img/slackbot_512.png",
                "status_text_canonical": "",
                "team": "T04LZ247MCK",
            },
            "is_admin": False,
            "is_owner": False,
            "is_primary_owner": False,
            "is_restricted": False,
            "is_ultra_restricted": False,
            "is_bot": False,
            "is_app_user": False,
            "updated": 0,
            "is_email_confirmed": False,
            "who_can_share_contact_card": "EVERYONE",
        },
        {
            "id": "U04LZ5K7ML2",
            "team_id": "T04LZ247MCK",
            "name": "hongreat95",
            "deleted": False,
            "color": "9f69e7",
            "real_name": "hongreat95",
            "tz": "Asia/Seoul",
            "tz_label": "Korea Standard Time",
            "tz_offset": 32400,
            "profile": {
                "title": "",
                "phone": "",
                "skype": "",
                "real_name": "hongreat95",
                "real_name_normalized": "hongreat95",
                "display_name": "",
                "display_name_normalized": "",
                "fields": None,
                "status_text": "",
                "status_emoji": "",
                "status_emoji_display_info": [],
                "status_expiration": 0,
                "avatar_hash": "g6a2f894e423",
                "email": "hongreat95@gmail.com",
                "first_name": "hongreat95",
                "last_name": "",
                "image_24": "https://secure.gravatar.com/avatar/6a2f894e423d89bfde38507bb15cbb5d.jpg?s=24&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0023-24.png",
                "image_32": "https://secure.gravatar.com/avatar/6a2f894e423d89bfde38507bb15cbb5d.jpg?s=32&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0023-32.png",
                "image_48": "https://secure.gravatar.com/avatar/6a2f894e423d89bfde38507bb15cbb5d.jpg?s=48&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0023-48.png",
                "image_72": "https://secure.gravatar.com/avatar/6a2f894e423d89bfde38507bb15cbb5d.jpg?s=72&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0023-72.png",
                "image_192": "https://secure.gravatar.com/avatar/6a2f894e423d89bfde38507bb15cbb5d.jpg?s=192&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0023-192.png",
                "image_512": "https://secure.gravatar.com/avatar/6a2f894e423d89bfde38507bb15cbb5d.jpg?s=512&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0023-512.png",
                "status_text_canonical": "",
                "team": "T04LZ247MCK",
            },
            "is_admin": True,
            "is_owner": True,
            "is_primary_owner": True,
            "is_restricted": False,
            "is_ultra_restricted": False,
            "is_bot": False,
            "is_app_user": False,
            "updated": 1674896110,
            "is_email_confirmed": True,
            "who_can_share_contact_card": "EVERYONE",
        },
        {
            "id": "U04M1KCSB1A",
            "team_id": "T04LZ247MCK",
            "name": "notion_notifications",
            "deleted": False,
            "color": "4bbe2e",
            "real_name": "Notion Notifications",
            "tz": "America/Los_Angeles",
            "tz_label": "Pacific Standard Time",
            "tz_offset": -28800,
            "profile": {
                "title": "",
                "phone": "",
                "skype": "",
                "real_name": "Notion Notifications",
                "real_name_normalized": "Notion Notifications",
                "display_name": "",
                "display_name_normalized": "",
                "fields": None,
                "status_text": "",
                "status_emoji": "",
                "status_emoji_display_info": [],
                "status_expiration": 0,
                "avatar_hash": "8e33f2a03e3c",
                "api_app_id": "A0VK5EP7Z",
                "always_active": False,
                "image_original": "https://avatars.slack-edge.com/2023-01-28/4698653743335_8e33f2a03e3c020be12d_original.png",
                "is_custom_image": True,
                "bot_id": "B04LSHBNZPY",
                "first_name": "Notion",
                "last_name": "Notifications",
                "image_24": "https://avatars.slack-edge.com/2023-01-28/4698653743335_8e33f2a03e3c020be12d_24.png",
                "image_32": "https://avatars.slack-edge.com/2023-01-28/4698653743335_8e33f2a03e3c020be12d_32.png",
                "image_48": "https://avatars.slack-edge.com/2023-01-28/4698653743335_8e33f2a03e3c020be12d_48.png",
                "image_72": "https://avatars.slack-edge.com/2023-01-28/4698653743335_8e33f2a03e3c020be12d_72.png",
                "image_192": "https://avatars.slack-edge.com/2023-01-28/4698653743335_8e33f2a03e3c020be12d_192.png",
                "image_512": "https://avatars.slack-edge.com/2023-01-28/4698653743335_8e33f2a03e3c020be12d_512.png",
                "image_1024": "https://avatars.slack-edge.com/2023-01-28/4698653743335_8e33f2a03e3c020be12d_1024.png",
                "status_text_canonical": "",
                "team": "T04LZ247MCK",
            },
            "is_admin": False,
            "is_owner": False,
            "is_primary_owner": False,
            "is_restricted": False,
            "is_ultra_restricted": False,
            "is_bot": True,
            "is_app_user": False,
            "updated": 1674896211,
            "is_email_confirmed": False,
            "who_can_share_contact_card": "EVERYONE",
        },
        {
            "id": "U04QJQHSN1W",
            "team_id": "T04LZ247MCK",
            "name": "toktokbotdev",
            "deleted": False,
            "color": "3c989f",
            "real_name": "TokTokBot_dev",
            "tz": "America/Los_Angeles",
            "tz_label": "Pacific Standard Time",
            "tz_offset": -28800,
            "profile": {
                "title": "",
                "phone": "",
                "skype": "",
                "real_name": "TokTokBot_dev",
                "real_name_normalized": "TokTokBot_dev",
                "display_name": "",
                "display_name_normalized": "",
                "fields": None,
                "status_text": "",
                "status_emoji": "",
                "status_emoji_display_info": [],
                "status_expiration": 0,
                "avatar_hash": "gd3e29ee4f4b",
                "api_app_id": "A04PS5RUCJZ",
                "always_active": False,
                "bot_id": "B04PNFZ6WTY",
                "first_name": "TokTokBot_dev",
                "last_name": "",
                "image_24": "https://secure.gravatar.com/avatar/d3e29ee4f4babea7c1860eaa98497262.jpg?s=24&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0025-24.png",
                "image_32": "https://secure.gravatar.com/avatar/d3e29ee4f4babea7c1860eaa98497262.jpg?s=32&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0025-32.png",
                "image_48": "https://secure.gravatar.com/avatar/d3e29ee4f4babea7c1860eaa98497262.jpg?s=48&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0025-48.png",
                "image_72": "https://secure.gravatar.com/avatar/d3e29ee4f4babea7c1860eaa98497262.jpg?s=72&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0025-72.png",
                "image_192": "https://secure.gravatar.com/avatar/d3e29ee4f4babea7c1860eaa98497262.jpg?s=192&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0025-192.png",
                "image_512": "https://secure.gravatar.com/avatar/d3e29ee4f4babea7c1860eaa98497262.jpg?s=512&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0025-512.png",
                "status_text_canonical": "",
                "team": "T04LZ247MCK",
            },
            "is_admin": False,
            "is_owner": False,
            "is_primary_owner": False,
            "is_restricted": False,
            "is_ultra_restricted": False,
            "is_bot": True,
            "is_app_user": False,
            "updated": 1676513239,
            "is_email_confirmed": False,
            "who_can_share_contact_card": "EVERYONE",
        },
    ],
    "cache_ts": 1676882921,
    "response_metadata": {"next_cursor": ""},
}


# members(iter)-["id"]/profile["email"]

members = check["members"]
user_information = {}
for one_member in members:
    user_id = one_member["id"]
    profile = one_member.get("profile")
    if profile:
        email = one_member.get("profile").get("email")
        if email:
            user_information["email"] = user_id
