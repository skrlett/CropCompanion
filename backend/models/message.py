from pydantic import BaseModel

class Messages(BaseModel):
    uuid: str
    timestamp: str 
    user_id: str 
    session_id: str
    user_chat: str 
    ai_chat: str 