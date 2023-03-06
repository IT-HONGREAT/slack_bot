from fastapi import FastAPI
from slack_bolt.adapter.asgi import SlackRequestHandler

from bolt.app import bolt_app
from router_fastapi import apis

# TODO
"""

fastapi의 apirouter 적용으로 flask의 blueprint처럼 활용가능한지 확인.

fastapi call 시 slack app call 되는점을 이용할것.
    slack api call 시 event handle이 안되는 점 파악하고 개선할것. 

"""


api = FastAPI()
app_handler = SlackRequestHandler(bolt_app)
api.include_router(apis.router)


# uvicorn 모듈이름:api --reload --port 3000 --log-level warning
