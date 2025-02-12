from pydantic import BaseModel
from typing import List
from datetime import datetime

class Message(BaseModel):
    timestamp: datetime
    user_chat: str 
    ai_chat: str 

class ChatSession(BaseModel):
    _id: str
    user_id: str
    timestamp: datetime
    message: List[Message]