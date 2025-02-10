from fastapi import HTTPException
from pymongo import MongoClient
from database.mongodb import users_collection
from models.user import User

def get_user(username: str):
    return get_user_by_username(username)

def get_user_by_username(username: str):
    # Retrieve a user from the database by username.
    users = users_collection.find({"username": username}).to_list()

    for user in users:
        user["_id"] = str(user["_id"])

    user = User(**users[0])
    return user

def save_user(user_data: User):
    # Insert a user into the database.
    return users_collection.insert_one(user_data.model_dump())

def register_user(user_data: User):
    # Register a new user after validating the username.
    # Check if the username already exists
    existing_user = get_user_by_username(user_data["username"])
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    # Save the new user to the database
    result = save_user(user_data)  # Save user data directly
    return result.inserted_id