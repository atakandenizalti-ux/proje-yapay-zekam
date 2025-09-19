import os
import subprocess
import time

def trigger_command():
    print("🔔 Wake word bulundu, asenkron alt süreç başlatılıyor…")

    # Bu dosyanın bulunduğu dizin
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # multi_model_voice.py'nin gerçek yolu
    target_script = os.path.join(script_dir, "multi_model_voice.py")
    print(f"▶️ Çağrılacak betik: {target_script}")

    # Alt süreci aynen aynı pencereye gönder, PATH veya %USERPROFILE% kullanma
    subprocess.Popen(
        ["python", target_script],
        cwd=script_dir
    )

    print("🔁 Wake word moduna geri dönülüyor...\n")

def listen_loop():
    print("🎧 Başladı, dinliyor… (Çıkmak için 'çıkış' yaz ve Enter)")
    while True:
        detected = input("> ").strip().lower()
        if detected == "çıkış":
            print("👋 Dinleme döngüsünden çıkılıyor. Program sonlanıyor.")
            break
        if "hey asistan" in detected:
            trigger_command()

if __name__ == "__main__":
    listen_loop()