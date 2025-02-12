from fastapi import HTTPException
from pymongo import MongoClient
from database.mongodb import messages_collection
from backend.models.chats import Message, ChatSession

def get_all_messages():
    messages_collection.find()

'''def get_all_messages_in_session():'''
    
def get_last_10_messages():
    messages = messages_collection.find().sort("uuid", -1).limit(10)

    messages_list = [Message(**message) for message in messages]
    return messages_list

def save_message(message_data: Message):
    
    # Insert a chat message into the database.
    return messages_collection.insert_one(message_data.model_dump())