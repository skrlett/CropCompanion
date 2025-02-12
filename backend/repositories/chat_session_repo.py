from fastapi import HTTPException
from pymongo import MongoClient
from database.mongodb import sessions_collection
from backend.models.chats import ChatSession

def create_session(session_data: ChatSession):
    return sessions_collection.insert_one(session_data.model_dump())

def clear_chat_history():
    sessions_collection.delete_many({})

def clear_chat_history_current_user(user_id):
    sessions_collection.delete_many({"user_id": user_id})