"""
Este módulo contiene pruebas para la API de Spotify utilizando pytest.
"""
import os
import requests
from dotenv import load_dotenv
BASE_URL = "https://api.genius.com"
load_dotenv()  # Cargar variables desde .env
ACCESS_TOKEN = os.getenv("GENIUS_ACCESS_TOKEN")

if not ACCESS_TOKEN:
    raise ValueError("El token de acceso no está definido en el archivo .env.")

HEADERS = {"Authorization": f"Bearer {ACCESS_TOKEN}"}


def test_get_song():
    """Prueba que busca una canción en la API de Spotify."""
    song_id = 378195  # ID de "Bohemian Rhapsody"
    response = requests.get(f"{BASE_URL}/songs/{song_id}", headers=HEADERS,timeout=10)
    assert response.status_code == 200
    assert "response" in response.json()
    assert response.json()["response"]["song"]["id"] == song_id

def test_get_artist():
    """Prueba que busca un artista en la API de Spotify."""
    artist_id = 16775  # ID de Queen
    response = requests.get(f"{BASE_URL}/artists/{artist_id}", headers=HEADERS,timeout=10)
    assert response.status_code == 200
    assert "response" in response.json()
    assert response.json()["response"]["artist"]["id"] == artist_id

def test_get_artist_songs():
    """Prueba que busca canciones de un artista en la API de Spotify."""
    artist_id = 16775  # ID de Queen
    params = {"per_page": 5, "page": 1}
    response = requests.get(f"{BASE_URL}/artists/{artist_id}/songs", headers=HEADERS, params=params,timeout=10)
    assert response.status_code == 200
    assert "response" in response.json()
    assert len(response.json()["response"]["songs"]) > 0

def test_get_annotation():
    """Prueba que busca anotaciones."""
    annotation_id = 6737660  # Ejemplo de anotación
    response = requests.get(f"{BASE_URL}/annotations/{annotation_id}", headers=HEADERS,timeout=10)
    assert response.status_code == 200
    assert "response" in response.json()
    assert response.json()["response"]["annotation"]["id"] == annotation_id
