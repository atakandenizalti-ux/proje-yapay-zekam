import pytest
from tts import TTS

def test_tts_play_runs(monkeypatch):
    tts = TTS()

    # edge_tts.Communicate.save metodunu sahte hale getiriyoruz
    class DummyCommunicate:
        async def save(self, file):
            return None

    monkeypatch.setattr("edge_tts.Communicate", lambda *a, **kw: DummyCommunicate())

    import asyncio
    try:
        asyncio.run(tts.play("test cümlesi"))
    except Exception as e:
        pytest.fail(f"TTS play hata verdi: {e}")