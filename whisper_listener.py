import whisper
import sounddevice as sd
import numpy as np
import queue
import threading
import tempfile
import os
import subprocess
import scipy.io.wavfile

model = whisper.load_model("base")
wake_word = "hey asistan"
q = queue.Queue()

def audio_callback(indata, frames, time, status):
    q.put(indata.copy())

def listen_and_transcribe():
    with sd.InputStream(samplerate=16000, channels=1, callback=audio_callback):
        print("🎧 Mikrofon açık, wake word bekleniyor...")
        while True:
            audio = np.concatenate([q.get() for _ in range(50)])
            temp_path = os.path.join(tempfile.gettempdir(), "temp.wav")
            scipy.io.wavfile.write(temp_path, 16000, audio)
            result = model.transcribe(temp_path, language="tr")
            text = result["text"].lower()
            print("🗣️ Algılanan:", text)
            if wake_word in text:
                print("✅ Wake word algılandı! Komut moduna geçiliyor...")
                subprocess.run(["python", "%USERPROFILE%\\Desktop\\multi_model_voice.py"])
                print("🔁 Wake word moduna geri dönülüyor...")

listen_and_transcribe()
