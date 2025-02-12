from pydantic import BaseModel

class User(BaseModel):
    user_id: str
    username: str
    email: str
    first_name: str
    last_name: str
    disabled: bool | None = None
    hashed_password: str
