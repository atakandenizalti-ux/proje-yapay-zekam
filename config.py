# config.py - YAPILANDIRMA AYARLARI
import os
from pathlib import Path

# Ses Ayarları
STT_TIMEOUT = 5
STT_PHRASE_LIMIT = 7
WAKE_WORD = "hey asistan"

# Model Ayarları
MODEL_API_URL = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "mistral"  # "turkish-llama" veya "turkish-mistral" yapabilirsin

# TTS Ayarları
VOICE = "tr-TR-AhmetNeural"
TTS_RATE = "+20%"

# Dosya Yolları
BASE_DIR = Path(__file__).parent
TEMP_DIR = BASE_DIR / "temp"
LOG_DIR = BASE_DIR / "logs"

# Klasörleri oluştur
TEMP_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)