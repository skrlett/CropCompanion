from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from config import MONGO_DB_NAME, URI

try:
    # Connect to MongoDB with Stable API v1
    client = MongoClient(URI, server_api=ServerApi('1'))

    # Access the database
    db = client[MONGO_DB_NAME]

    # Collections
    users_collection = db["users"]
    messages_collection = db["messages"]
    sessions_collection = db["sessions"]
    
    # Check the connection by listing collections
    print(f"Connected to MongoDB. Collections: {db.list_collection_names()}")

except Exception as e:
    print(f"Error connecting to MongoDB: {e}")