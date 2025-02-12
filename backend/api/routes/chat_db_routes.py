import uuid
from fastapi import APIRouter, HTTPException, Depends
from typing import List, Annotated
from models.user import User
from repositories.message_repo import get_all_sessions, get_last_10_messages, save_message
from core.auth import get_current_active_user
from models.message import ChatSession, Message
from datetime import datetime

router = APIRouter()

@router.post("/api/create_new_chat_session")
async def create_new_chat_session(current_user: Annotated[User, Depends(get_current_active_user)]):

    id = str(uuid.uuid4())
    newChatSession = ChatSession(
        chat_session_id = id,
        user_id=current_user.user_id,
        timestamp=datetime.now(),
        messages=[]
    )
    
    save_message(newChatSession)

    return {"chat_session_id": id}

@router.get("/api/all_chat_sessions")
async def create_new_chat_session(current_user: Annotated[User, Depends(get_current_active_user)]):
    
    return get_all_sessions(current_user.user_id)
