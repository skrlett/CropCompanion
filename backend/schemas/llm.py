from pydantic import BaseModel

class Query(BaseModel):
    user_id: str
    prompt: str
    system: str = "You help farmers achieve their goals of sustainable farming"
    model: str = "llama3.2:1b"
    stream: bool = True
