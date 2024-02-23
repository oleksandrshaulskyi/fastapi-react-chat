from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from application.database import Message, messages_collection


messages_router = InferringRouter(prefix='/messages')


@cbv(router=messages_router)
class MessageCBV:

    @messages_router.get('/')
    async def get_messages(self) -> list[Message]:
        pass

    @messages_router.post('/create-message')
    async def create_message(self) -> Message:
        pass
