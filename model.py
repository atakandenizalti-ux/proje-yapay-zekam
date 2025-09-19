# model.py - TÜRKÇE YAPAY ZEKA MODELİ
import requests
from config import MODEL_API_URL, DEFAULT_MODEL  # DEFAULT_MODEL'i import ettik

def select_model(prompt: str) -> str:
    # ARTIK CONFIG'DEN ALIYORUZ
    return DEFAULT_MODEL

def query_model(command: str) -> str:
    model = select_model(command)
    
    # ÇOK GÜÇLÜ TÜRKÇE PROMPT
    turkish_prompt = f"""
    SEN BİR TÜRKÇE ASİSTANSIN. SADECE TÜRKÇE KONUŞ!

    KESİNLİKLE YASAKLAR:
    - İngilizce kelime kullanma
    - Parantez içi açıklama yapma  
    - Çeviri ekleme
    - Not yazma

    ZORUNLU KURALLAR:
    - Sadece Türkçe konuş
    - Doğal ve günlük dil kullan
    - Kısa ve net olsun
    - Samimi ol

    SORU: {command}
    YANIT:"""
    
    payload = {
        "model": model,
        "prompt": turkish_prompt,
        "stream": False,
        "options": {
            "temperature": 0.3,
            "max_tokens": 100,
        }
    }
    
    try:
        response = requests.post(MODEL_API_URL, json=payload, timeout=30)
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except Exception as e:
        return f"Üzgünüm, bir hata oluştu: {str(e)}"