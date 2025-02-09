import uuid
from fastapi import APIRouter
from fastapi import HTTPException

from core.security import get_password_hash
from repositories.user_repo import get_user_by_username, save_user
from schemas.user import User as SchemaUser
from models.user import User as ModelUser

router = APIRouter()


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