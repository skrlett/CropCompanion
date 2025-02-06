from fastapi import FastAPI, Depends
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from langchain_ollama import OllamaLLM

app = FastAPI()

# Add CORS middleware
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'], allow_headers=['*'])

# Store memory per user (Basic In-Memory Storage)
conversation_memory = {}

class Query(BaseModel):
    user_id: str = "1"
    prompt: str
    system: str = "You help farmers achieve their goals of sustainable farming"
    model: str = "llama3.2"
    stream: bool = True

async def stream_answer(system_prompt, model, question, history):

    # Initialize Ollama
    ollama = OllamaLLM(base_url="http://localhost:11434", model=model, cache=True)

    full_prompt = f"""System: {system_prompt}
                        Conversation history (for context only, do not answer these again):
                        \nPrevious conversation: {history}\nUser: {question}\nAssistant:"""
    
    async for chunk in ollama.astream(full_prompt):
        yield chunk

@app.post('/generate')
async def stream_response_from_llm(query: Query):
    user_id = query.user_id
    history = conversation_memory.get(user_id, "")

    # Update memory with new interaction
    history += f"\nUser: {query.prompt}\n"
    conversation_memory[user_id] = history

    generator = stream_answer(query.system, query.model, query.prompt, history)
    return StreamingResponse(generator, media_type="text/event-stream; charset=utf-8")

@app.post('/clear_memory')
def delete_memory():
    conversation_memory = {}

    return {"value":"mem cache has been cleared"}
