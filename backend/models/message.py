from pydantic import BaseModel
from typing import List
from datetime import datetime

class Message(BaseModel):
    timestamp: datetime
    user_chat: str
    ai_response: str

class ChatSession(BaseModel):
    chat_session_id: str
    user_id: str
    timestamp: datetime
    messages: List[Message]