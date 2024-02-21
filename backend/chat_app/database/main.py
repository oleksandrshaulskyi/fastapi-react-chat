from motor.motor_asyncio import AsyncIOMotorClient


database_client = AsyncIOMotorClient('mongodb://database:27017')


db = database_client['main_database']

collection = db['main_collection']
