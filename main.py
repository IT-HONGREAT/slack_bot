from fastapi import FastAPI

from notion.reservation import Notion

app = FastAPI()
notion = Notion()


@app.get("/reservation")
async def read_reservation():
    response = notion.get_reservation(database_name="reservation")  # TODO description database_name
    return response


# TODO remove when finish test
response = notion.get_reservation(database_name="reservation")
