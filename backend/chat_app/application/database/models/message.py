from datetime import datetime

from pydantic import BaseModel


class Message(BaseModel):
    message_id: int
    sent_at: datetime
    message_text: str
    sender_id: int
    recepient_id: int
    was_sent: bool
    was_delivered: bool
    was_read: bool
