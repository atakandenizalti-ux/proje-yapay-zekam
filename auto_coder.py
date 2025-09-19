# auto_coder.py - OTOMASYON ASİSTANI
import pyautogui
import time
import subprocess
from PIL import ImageGrab

class AutoCoder:
    def __init__(self):
        self.screen_width, self.screen_height = pyautogui.size()
        print(f"🖥️ Ekran boyutu: {self.screen_width}x{self.screen_height}")
    
    def click(self, x, y):
        pyautogui.click(x, y)
        print(f"🖱️ Tıklandı: ({x}, {y})")
    
    def type_text(self, text):
        pyautogui.write(text, interval=0.1)
        print(f"⌨️ Yazıldı: {text}")
    
    def screenshot(self, filename="screenshot.png"):
        screenshot = ImageGrab.grab()
        screenshot.save(filename)
        print(f"📸 Ekran görüntüsü kaydedildi: {filename}")
        return filename
    
    def run_command(self, command):
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print(f"⚡ Komut çalıştırıldı: {command}")
        return result.stdout

# Test
if __name__ == "__main__":
    bot = AutoCoder()
    print("🤖 AutoCoder hazır!")
    
    # Ekran görüntüsü al
    bot.screenshot("test_screenshot.png")
    
    # VS Code'u açmayı dene
    try:
        bot.run_command("code .")
        print("✅ VS Code açıldı!")
    except:
        print("⚠️ VS Code açılamadı, normal")