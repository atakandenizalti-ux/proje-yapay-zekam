import asyncio
import datetime
from stt import STT
from tts import TTS
from model import query_model


class Assistant:
    def __init__(self):
        self.stt = STT()
        self.tts = TTS()

    def run(self, max_loops: int = None):
        """
        Asistanı çalıştırır.
        - Wake-word: "hey asistan"
        - Komutlar: "ne haber", "saat kaç", "çıkış"
        - Diğer her şey: modele gönderilir
        - max_loops: testler için döngü sınırı
        """
        loops = 0
        while True:
            text = self.stt.listen()
            if text and "hey asistan" in text.lower():
                print("🔔 Wake word algılandı, komut dinleniyor…")
                command = self.stt.listen()
                if command:
                    cmd = command.lower()

                    # 🔹 Hazır komutlar
                    if "ne haber" in cmd:
                        response = "İyiyim, sen nasılsın?"
                    elif "saat kaç" in cmd:
                        now = datetime.datetime.now().strftime("%H:%M")
                        response = f"Saat şu an {now}"
                    elif "çıkış" in cmd:
                        response = "Görüşürüz!"
                        asyncio.run(self.tts.play(response))
                        break
                    else:
                        # 🔹 Diğer her şey modeli çağırır
                        response = query_model(command)

                    if response:
                        asyncio.run(self.tts.play(response))
                else:
                    print("❌ Komut anlaşılmadı; lütfen yeniden deneyin.")

            # Testlerde sonsuz döngüye girmemesi için
            if max_loops is not None:
                loops += 1
                if loops >= max_loops:
                    break