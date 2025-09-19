import subprocess
import json

def komut_al():
    return input("Görev verin: ")

def analiz_et_yerel(cmd_text, model="deepseek-r1"):
    proc = subprocess.run(
        ["ollama", "run", model, "--json", "--prompt", cmd_text],
        capture_output=True, text=True, check=True
    )
    out = json.loads(proc.stdout)
    content = out["choices"][0]["message"]["content"]
    return [line.strip() for line in content.splitlines() if line.strip()]

def yurut(steps):
    for step in steps:
        print(f">>> {step}")
        res = subprocess.run(step, shell=True)
        if res.returncode != 0:
            print(f"Hata: '{step}' adımı başarısız.")
            break

if __name__ == "__main__":
    cmd = komut_al()
    adimlar = analiz_et_yerel(cmd)
    yurut(adimlar)
