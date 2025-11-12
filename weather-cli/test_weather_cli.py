import pytest
import requests
from weather_cli import get_api_key, fetch_weather, print_weather


# --- Helpers ---

class DummyResponse:
    def __init__(self, status_code, json_data=None):
        self.status_code = status_code
        self._json = json_data or {}

    def json(self):
        return self._json

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"{self.status_code} Error")


# --- Tests ---

def test_get_api_key_env(monkeypatch):
    monkeypatch.setenv("OPENWEATHER_API_KEY", "dummy")
    assert get_api_key() == "dummy"


def test_get_api_key_missing(monkeypatch):
    monkeypatch.delenv("OPENWEATHER_API_KEY", raising=False)
    with pytest.raises(SystemExit):
        get_api_key()


def test_fetch_weather_valid(monkeypatch):
    dummy_json = {
        "name": "Madrid",
        "main": {"temp": 20},
        "weather": [{"description": "soleado"}]
    }

    def mock_get(*a, **k):
        return DummyResponse(200, dummy_json)

    monkeypatch.setattr(requests, "get", mock_get)
    data = fetch_weather("Madrid", "dummy")
    assert data["name"] == "Madrid"
    assert data["main"]["temp"] == 20
    assert data["weather"][0]["description"] == "soleado"


def test_fetch_weather_city_not_found(monkeypatch):
    def mock_get(*a, **k):
        return DummyResponse(404)

    monkeypatch.setattr(requests, "get", mock_get)
    with pytest.raises(SystemExit):
        fetch_weather("NoExiste", "dummy")


def test_fetch_weather_invalid_key(monkeypatch):
    def mock_get(*a, **k):
        return DummyResponse(401)

    monkeypatch.setattr(requests, "get", mock_get)
    with pytest.raises(SystemExit):
        fetch_weather("Madrid", "badkey")


def test_fetch_weather_network_error(monkeypatch):
    def mock_get(*a, **k):
        raise requests.ConnectionError("fail")

    monkeypatch.setattr(requests, "get", mock_get)
    with pytest.raises(SystemExit):
        fetch_weather("Madrid", "dummy")


def test_print_weather(capsys):
    data = {
        "name": "Madrid",
        "main": {"temp": 22},
        "weather": [{"description": "soleado"}]
    }
    print_weather(data)
    out = capsys.readouterr().out
    assert "Ciudad: Madrid" in out
    assert "Temperatura: 22°C" in out
    assert "Clima: Soleado" in out
