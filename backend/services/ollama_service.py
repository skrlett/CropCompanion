import json
from fastapi.responses import StreamingResponse
from datetime import datetime
from langchain_ollama import OllamaLLM
from models.message import Message, ChatSession
from repositories.message_repo import get_last_10_messages, get_message_session, update_message_list
from database.mongodb import messages_collection

conversation_memory = {}

async def stream_answer(system_prompt, model, question, history, chat_session_id: str, user_id: str):
    ollama = OllamaLLM(base_url="http://localhost:11434", model=model, cache=True)
    full_prompt = f"System: {system_prompt}\nConversation history:\n{history}\nUser: {question}\nAssistant:"

    response = ""
    async for chunk in ollama.astream(full_prompt):
        response += chunk
        yield chunk
    
    # create a new message object and store
    message = Message(
        timestamp=datetime.now(),
        user_chat=question,
        ai_response=response
    )

    # get the current_chat_object
    all_chat: ChatSession = get_message_session(chat_session_id=chat_session_id)
    all_chat["_id"] = str(all_chat["_id"])
    all_messages = all_chat["messages"]
    all_messages.append(message.dict())

    # print(all_messages)

    # save all_chat_messages
    update_message_list(chat_session_id = chat_session_id, messages=all_messages)

def update_conversation_memory(user_id: str, chat_session_id: str):
    history = get_last_10_messages(user_id=user_id, chat_session_id=chat_session_id)
    
    return history