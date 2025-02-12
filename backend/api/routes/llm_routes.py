from typing import Annotated
from models.user import User
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from services.ollama_service import stream_answer, update_conversation_memory
from schemas.llm import Query
from core.auth import get_current_active_user, get_current_user
router = APIRouter()

@router.post('/generate')
def stream_response_from_llm(query: Query, chat_session_id: str, user_id: str, current_user: Annotated[User, Depends(get_current_active_user)]):
    history = update_conversation_memory(user_id=user_id, chat_session_id=chat_session_id)
    generator = stream_answer(query.system, query.model, query.prompt, history, chat_session_id, user_id)
    return StreamingResponse(generator, media_type="text/event-stream; charset=utf-8")
