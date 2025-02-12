from typing import List
from fastapi import HTTPException
from pymongo import MongoClient
from database.mongodb import messages_collection
from models.message import ChatSession, Message

def get_last_10_messages(user_id: str, chat_session_id: str):
    messages = list(messages_collection.find({"chat_session_id": chat_session_id, "user_id": user_id}).sort("timestamp", -1).limit(10))

    # messages_list = [Message(**message) for message in messages]
    messages_list_sting = ""
    for message in messages:
        message['_id'] = str(message['_id'])
        messages_list_sting += "user_chat: " + message["user_chat"] + "response: " + message["ai_response"]
    
    return messages_list_sting

def save_message(chat_message_data: ChatSession):
    
    # chat_session = ChatSession(**chat_message_data.model_dump())
    # Insert a chat message into the database.
    return messages_collection.insert_one(chat_message_data.model_dump())

def get_message_session(chat_session_id: str):
    chat_session = list(messages_collection.find({"chat_session_id": chat_session_id}))

    if not chat_session:
        raise HTTPException(status_code=404, detail="Chat session not found")
    
    for session in chat_session:
        session['_id'] = str(session['_id'])
    
    return chat_session[0]

def update_message_list(chat_session_id: str, messages: List[Message]):

    # message_dicts = [msg.model_dump() for msg in messages]
    # print(messages)
    messages_collection.update_one({"chat_session_id": chat_session_id}, {"$set": {"messages": messages}})

def get_all_sessions(user_id: str):
    chat_sessions = list(messages_collection.find({"user_id": user_id}))

    for session in chat_sessions:
        session['_id'] = str(session['_id'])

    return chat_sessions

