import sys
import io
import speech_recognition as sr
import requests
import asyncio
from edge_tts import Communicate
import pygame
import tempfile
import uuid
import os

# UTF-8 çıktı sarması
sys.stdout = io.TextIOWrapper(
    sys.stdout.buffer,
    encoding="utf-8",
    errors="ignore"
)

def select_model(prompt):
    prompt_lower = prompt.lower()
    tech = ["kod","python","api","fonksiyon","hata","pip","terminal"]
    info = ["özet","bilgi","nedir","nasıl","özellikleri"]
    if any(w in prompt_lower for w in tech):
        return "deepseek-coder:6.7b"
    if any(w in prompt_lower for w in info):
        return "mistral"
    return "llama3"

def query_model(prompt, model):
    chat_prompt = f"Konuşma dilinde, akıcı ve net cümlelerle yanıt ver: {prompt}"
    resp = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": chat_prompt, "stream": False}
    )
    return resp.json().get("response", "")

async def speak(text):
    # SSML ile %20 hız artışı
    ssml = f"<speak><prosody rate='+20%'>{text}</prosody></speak>"
    filename = os.path.join(tempfile.gettempdir(), f"{uuid.uuid4()}.mp3")

    print("🔊 Ses oynatılıyor…")
    # 'format' parametresini kaldırdık
    await Communicate(ssml, voice="tr-TR-AhmetNeural").save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        await asyncio.sleep(0.1)
    # os.remove(filename)

def main():
    recognizer = sr.Recognizer()

    # Ortam gürültüsüne göre kalibrasyon
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("🎙️ Konuşabilirsiniz... (5s içinde başlatın)")
        try:
            audio = recognizer.listen(
                source, timeout=5, phrase_time_limit=7
            )
        except sr.WaitTimeoutError:
            print("⏱️ Süre doldu, ses algılanamadı.")
            return

    # Speech-to-Text
    try:
        command = recognizer.recognize_google(audio, language="tr-TR")
        print("🗣️ Algılanan komut:", command)
    except sr.UnknownValueError:
        print("❌ Konuşmanızı anlayamadım, lütfen tekrar deneyin.")
        return
    except sr.RequestError as e:
        print(f"❌ Google API hatası: {e}")
        return

    # Model seçimi ve sorgu
    model = select_model(command)
    print("🧠 Seçilen model:", model)
    cevap = query_model(command, model)
    print("🤖 Model cevabı:", cevap)

    # TTS ve oynatma
    try:
        asyncio.run(speak(cevap))
    except Exception as e:
        print("❌ TTS hatası:", e)

if __name__ == "__main__":
    main()