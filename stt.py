# stt.py
import speech_recognition as sr
from config import STT_TIMEOUT, STT_PHRASE_LIMIT

class STT:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as src:
            self.recognizer.adjust_for_ambient_noise(src, duration=1)
            print("🎙️ Dinleniyor... (5s içinde başlatın)")
            audio = self.recognizer.listen(
                src,
                timeout=STT_TIMEOUT,
                phrase_time_limit=STT_PHRASE_LIMIT
            )
        return audio

    def recognize(self, audio):
        text = self.recognizer.recognize_google(audio, language="tr-TR")
        print("🗣️ Algılanan metin:", text)
        return text