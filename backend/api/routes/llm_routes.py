from typing import Annotated
from models.user import User
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from services.ollama_service import stream_answer, update_conversation_memory, clear_memory
from schemas.llm import Query
from core.auth import get_current_active_user, get_current_user
router = APIRouter()

@router.post('/generate')
async def stream_response_from_llm(query: Query, current_user: Annotated[User, Depends(get_current_active_user)]):
    history = update_conversation_memory(query.user_id, query.prompt)
    generator = stream_answer(query.system, query.model, query.prompt, history)
    return StreamingResponse(generator, media_type="text/event-stream; charset=utf-8")

@router.post('/clear_memory')
def delete_memory(current_user: Annotated[User, Depends(get_current_active_user)]):
    clear_memory()
    return {"message": "Memory cache cleared"}
