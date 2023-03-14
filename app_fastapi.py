from fastapi import FastAPI
from slack_bolt.adapter.asgi import SlackRequestHandler

from bolt_python.app import bolt_app
from router_fastapi import apis

api = FastAPI()
app_handler = SlackRequestHandler(bolt_app)
api.include_router(apis.router)


# uvicorn 모듈이름:api --reload --port 3000 --log-level warning
