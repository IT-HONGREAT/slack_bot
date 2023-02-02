from fastapi import FastAPI, Depends

from notion.app import Notion

app = FastAPI()
notion = Notion()


@app.get("/reservation")
async def read_reservation():
    response = notion.get_reservation(database_name="reservation")
    return response


# TODO setting
@app.post("/reservation")
async def create_reservation(notion_1=Depends(Notion)):
    response = notion_1.create_reservation(
        database_name="reservation",
        room="지니",
        title="팀 회의 등록",
        purpose="내부회의",
        start="2023-01-30T01:00:00",
        end="2023-01-30T16:00:00",
    )
    return response
