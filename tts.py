# tts.py
import asyncio
import tempfile
import uuid
import os
import pygame
from edge_tts import Communicate
from config import VOICE, TTS_RATE

class TTS:
    def __init__(self):
        # Pygame mixer bir kez başlatılır
        pygame.mixer.init()
        self.voice = VOICE
        self.rate = TTS_RATE

    async def play(self, text: str):
        # SSML ile hız ayarı
        ssml = f"<speak><prosody rate='{self.rate}'>{text}</prosody></speak>"
        # Geçici dosya adı
        filename = os.path.join(tempfile.gettempdir(), f"{uuid.uuid4()}.mp3")
        print("🔊 Ses oynatılıyor…")
        # TTS üret ve kaydet
        await Communicate(ssml, voice=self.voice).save(filename)
        # Oynatma
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            await asyncio.sleep(0.1)