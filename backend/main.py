from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import httpx

app = FastAPI()

class Query(BaseModel):
    prompt: str
    system: str = "You help farmer achieve their goals of sustainable farming"
    model: str = "llama3.2:1b"
    stream: bool = False

@app.post("/generate")
async def generate_text(query: Query):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                "http://localhost:11434/api/generate",
                json={"model": query.model, "prompt": query.prompt, "stream":query.stream, "system":query.system}
            )
            return {"generated_text": response.json()["response"]}
        except httpx.RequestError as e:
            raise HTTPException(status_code=500, detail=f"Error communicating with Ollama: {str(e)}")