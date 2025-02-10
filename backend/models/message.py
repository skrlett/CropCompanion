import uuid
from pydantic import BaseModel, Field

class Messages(BaseModel):
    uuid: str = Field(default_factory=uuid.uuid4, alias="_id")
    timestamp: str = Field(...)
    user_id: str = Field(...)
    session_id: str = Field(...)
    user_chat: str = Field(...)
    ai_chat: str = Field(...)