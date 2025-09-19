from model import select_model, query_model
import requests
import pytest

def test_select_model_code():
    assert select_model("kod örneği") == "deepseek-coder:6.7b"

def test_select_model_general():
    assert select_model("merhaba") == "deepseek-r1:7b"

def test_query_model_handles_error(monkeypatch):
    def fake_post(*args, **kwargs):
        raise requests.RequestException("network error")
    monkeypatch.setattr(requests, "post", fake_post)

    result = query_model("selam")
    assert result == ""  # hata durumunda boş string dönmeli