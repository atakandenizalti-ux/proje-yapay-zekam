# model.py - GÜNCELLENMİŞ TÜRKÇE DESTEKLİ
import requests
from config import MODEL_API_URL

def select_model(prompt: str) -> str:
    prompt_lower = prompt.lower()
    tech = ["kod", "python", "api", "fonksiyon", "hata", "pip", "terminal", "program"]
    info = ["özet", "bilgi", "nedir", "nasıl", "özellikleri", "açıkla", "anlat"]
    
    if any(word in prompt_lower for word in tech):
        return "deepseek-coder:6.7b"
    if any(word in prompt_lower for word in info):
        return "mistral"
    return "llama3"

def query_model(command: str) -> str:
    model = select_model(command)
    
    # Güçlü Türkçe promptu:
    turkish_prompt = f"""
    Lütfen sadece Türkçe yanıt ver. Yanıtın:
    - Tamamen Türkçe olsun
    - Akıcı ve doğal olsun  
    - Günlük konuşma diliyle yaz
    - Empatik ve samimi olsun
    
    Kullanıcı sorusu: {command}
    """
    
    payload = {
        "model": model,
        "prompt": turkish_prompt,
        "stream": False
    }
    
    try:
        response = requests.post(MODEL_API_URL, json=payload, timeout=30)
        response.raise_for_status()
        return response.json().get("response", "")
    except Exception as e:
        return f"Üzgünüm, bir hata oluştu: {str(e)}"