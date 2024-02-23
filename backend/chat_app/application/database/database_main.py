from motor.motor_asyncio import AsyncIOMotorClient

from application.settings.settings import settings


database_client = AsyncIOMotorClient(settings.mongodb_url)
messages_database = database_client.messages_database
messages_collection = messages_database.messages_collection

async def create_unique_index() -> None:
    await messages_collection.create_index('message_id', unique=True)
