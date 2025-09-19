import pytest
from stt import STT

def test_listen_returns_str(monkeypatch):
    stt = STT()

    # listen() fonksiyonunu sahte bir değer döndürecek şekilde patch’liyoruz
    monkeypatch.setattr(stt, "listen", lambda: "merhaba")

    result = stt.listen()
    assert isinstance(result, str)
    assert result == "merhaba"

def test_recognize_raises_on_none(monkeypatch):
    stt = STT()

    # recognize fonksiyonuna None verilirse hata fırlatmalı
    with pytest.raises(Exception):
        stt.recognize(None)