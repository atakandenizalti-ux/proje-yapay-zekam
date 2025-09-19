import pytest
import assistant

def test_assistant_wake_and_command(monkeypatch):
    assistant_obj = assistant.Assistant()

    # STT.listen sahte: önce wake-word, sonra komut
    responses = iter(["hey asistan", "merhaba"])
    monkeypatch.setattr(assistant_obj.stt, "listen", lambda: next(responses))

    # Model sahte: assistant modülündeki query_model kopyasını patch’le
    monkeypatch.setattr(assistant, "query_model", lambda cmd: "cevap")

    # TTS sahte: play çağrısını yakala
    called = {}
    async def fake_play(text):
        called["text"] = text
    monkeypatch.setattr(assistant_obj.tts, "play", fake_play)

    # Sonsuz döngüye girmesin diye max_loops parametresini kullanalım
    assistant_obj.run(max_loops=1)

    # Beklenen: modelden "cevap" dönmüş ve TTS'e gönderilmiş
    assert called.get("text") == "cevap"