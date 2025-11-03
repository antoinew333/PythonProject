import requests
import json
import base64
import streamlit as st

TOKEN = st.secrets["GITHUB_TOKEN"]
FILE_PATH = "plik_ksiazki.json"
GITHUB_REPO = "antoinew333/biblioteka"

def wczytaj_ksiazki():
    url = "https://api.github.com/repos/antoinew333/biblioteka"
    headers = {"Authorization": f"token {TOKEN}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        content = base64.b64decode(response.json()["content"]).decode("utf-8")
        return json.loads(content)
    else:
        return []

def zapisz_ksiazke(ksiazki):
    url = "https://api.github.com/repos/antoinew333/biblioteka"
    headers = {"Authorization": f"token {TOKEN}"}
    get_response = requests.get(url, headers=headers)
    sha = get_response.json()["sha"]
    new_content = base64.b64decode(json.dump(ksiazki, indent = 4, ensure_ascii = False).encode()).decode()
    data = {
        "message": "Aktualizacja pliku JSON",
        "content": new_content,
        "sha": sha
    }
    put_response = requests.put(url, headers=headers, data=json.dumps(data))
    return put_response.status_code == 200