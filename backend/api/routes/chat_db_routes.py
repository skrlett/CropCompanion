from fastapi import APIRouter, HTTPException
from typing import List, Annotated
from models.user import User
import uuid
from fastapi import APIRouter, Depends
from repositories.message_repo import get_all_messages, get_last_10_messages, save_message
from repositories.chat_session_repo import create_session, clear_chat_history, clear_chat_history_current_user
from backend.models.chats import Message, ChatSession
from datetime import datetime, timezone
from core.auth import get_current_active_user
import requests
router = APIRouter()

@router.post("/create_new_session")
async def create_new_session(current_user: Annotated[User, Depends(get_current_active_user)]):
    session_data = ChatSession(
        _id=str(uuid.uuid4()),
        user_id = current_user.user_id,
        timestamp = datetime.now(timezone.utc).isoformat(),
        message =
    )
    create_session(session_data)

@router.post("/clear_session_history")
async def delete_session_history_current_user(current_user: Annotated[User, Depends(get_current_active_user)]):
    clear_chat_history_current_user(current_user.user_id)

@router.post("/clear_session_history")
async def delete_all_sessions_all_users():
    clear_chat_history()


'''@router.post("/api/create_message")
async def create_message(message_data: Messages):
    chat_data = Messages(
        uuid: str
        timestamp = datetime.utcnow().isoformat()
        user_id: str 
        session_id: str
        user_chat: str 
        ai_chat: str 
        user_id=str(uuid.uuid4()),
        username=user_data.username,
        email=user_data.email,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        hashed_password=get_password_hash(user_data.password)
    )

    try:
        save_user(user_data_full)
        return {"message": "User registered successfully", "user_id": user_data_full.user_id}
    except Exception as e:
        return HTTPException(status_code=400, detail=f"Cannot create user: {str(e)}")

@router.post("/", response_description="Create a new Chat message", status_code=status.HTTP_201_CREATED, response_model=Messages)
def create_book(request: Request, book: Book = Body(...)):
    book = jsonable_encoder(book)
    new_book = request.app.database["books"].insert_one(book)
    created_book = request.app.database["books"].find_one(
        {"_id": new_book.inserted_id}
    )

    return created_book

@router.post("/api/register_user")
async def register_user(user_data: SchemaUser):

    user_data_full = ModelUser(
        user_id=str(uuid.uuid4()),
        username=user_data.username,
        email=user_data.email,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        hashed_password=get_password_hash(user_data.password)
    )

    try:
        save_user(user_data_full)
        return {"message": "User registered successfully", "user_id": user_data_full.user_id}
    except Exception as e:
        return HTTPException(status_code=400, detail=f"Cannot create user: {str(e)}")

@router.get("/api/get_user_by_username")
async def get_user(username: str):
    return get_user_by_username(username)

@router.get("/", response_description="List all books", response_model=List[Book])
def list_books(request: Request):
    books = list(request.app.database["books"].find(limit=100))
    return books

@router.get("/{id}", response_description="Get a single book by id", response_model=Book)
def find_book(id: str, request: Request):
    if (book := request.app.database["books"].find_one({"_id": id})) is not None:
        return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with ID {id} not found")'''