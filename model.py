# model.py
import requests
from config import MODEL_API_URL

def select_model(prompt: str) -> str:
    prompt_lower = prompt.lower()
    tech = ["kod", "python", "api", "fonksiyon", "hata", "pip", "terminal"]
    info = ["özet", "bilgi", "nedir", "nasıl", "özellikleri"]
    if any(word in prompt_lower for word in tech):
        return "deepseek-coder:6.7b"
    if any(word in prompt_lower for word in info):
        return "mistral"
    return "llama3"

def query_model(command: str) -> str:
    model = select_model(command)
    payload = {
        "model": model,
        "prompt": f"Konuşma dilinde, akıcı ve net cümlelerle yanıt ver: {command}",
        "stream": False
    }
    response = requests.post(MODEL_API_URL, json=payload)
    return response.json().get("response", "")