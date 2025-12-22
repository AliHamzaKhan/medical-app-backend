from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

# Shared properties
class MessageBase(BaseModel):
    message_content: Optional[str] = None
    timestamp: Optional[datetime] = None


# Properties to receive on item creation
class MessageCreate(MessageBase):
    sender_id: int
    receiver_id: int
    message_content: str


# Properties to receive on item update
class MessageUpdate(MessageBase):
    pass


# Properties shared by models in DB
class MessageInDBBase(MessageBase):
    id: int
    sender_id: int
    receiver_id: int

    model_config = ConfigDict(from_attributes=True)


# Properties to return to client
class Message(MessageInDBBase):
    pass


# Properties properties stored in DB
class MessageInDB(MessageInDBBase):
    pass
