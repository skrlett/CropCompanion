from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
