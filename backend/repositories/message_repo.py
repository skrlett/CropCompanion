from typing import List
from fastapi import HTTPException
from pymongo import MongoClient
from database.mongodb import messages_collection
from models.message import ChatSession, Message

def get_last_10_messages(user_id: str, chat_session_id: str):
    messages = messages_collection.find({"chat_session_id": chat_session_id, "user_id": user_id}).sort("timestamp", -1).limit(10)

    messages_list = [Message(**message) for message in messages]
    return messages_list

def save_message(chat_message_data: ChatSession):
    
    # Insert a chat message into the database.
    return messages_collection.insert_one(chat_message_data.model_dump())

def get_message_session(chat_session_id: str):
    chat_session = messages_collection.find({"chat_session_id": chat_session_id})

    if not chat_session:
        raise HTTPException(status_code=404, detail="Chat session not found")
    
    return chat_session.dump()

def update_message_list(_id: str, messages: List[Message]):
    message_dicts = [msg.model_dump() for msg in messages]
    messages_collection.update_one({"_id": _id}, {"$set": {"messages": message_dicts}})

