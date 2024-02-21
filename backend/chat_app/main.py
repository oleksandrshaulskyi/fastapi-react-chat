from bson import ObjectId

from fastapi import FastAPI

from backend.models import TestItem
from backend.database import db


application = FastAPI()


@application.get('/')
async def index(obj_id: str | None = None):
    r = await db.main_collection.find_one({'_id': ObjectId(obj_id)})
    return repr(r)


@application.post('/add')
async def add_item(item: TestItem):
    res = await db.main_collection.insert_one(item.model_dump())
    return repr(res.inserted_id)
