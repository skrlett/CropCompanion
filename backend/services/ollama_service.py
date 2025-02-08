from fastapi.responses import StreamingResponse
from langchain_ollama import OllamaLLM

conversation_memory = {}

async def stream_answer(system_prompt, model, question, history):
    ollama = OllamaLLM(base_url="http://localhost:11434", model=model, cache=True)
    full_prompt = f"System: {system_prompt}\nConversation history:\n{history}\nUser: {question}\nAssistant:"
    async for chunk in ollama.astream(full_prompt):
        yield chunk

def update_conversation_memory(user_id: str, prompt: str):
    history = conversation_memory.get(user_id, "")
    history += f"\nUser: {prompt}\n"
    conversation_memory[user_id] = history
    return history

def clear_memory():
    conversation_memory.clear()