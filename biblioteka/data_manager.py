import requests
import json
import base64
import streamlit as st


TOKEN = st.secrets["GITHUB_TOKEN"]
FILE_PATH = "plik_ksiazki.json"
GITHUB_REPO = "antoinew333/biblioteka"
URL = "https://api.github.com/repos/antoinew333/biblioteka/contents/plik_ksiazki.json"

def wczytaj_ksiazki():
    headers = {"Authorization": f"token {TOKEN}"}
    response = requests.get(URL, headers=headers)
    if response.status_code == 200:
        data = response.json()
        content = base64.b64decode(data["contents"]).decode("utf-8")
        return json.loads(content)
    else:
        st.warning("Nie udało się wczytać danych z GitHuba")
        return []

def zapisz_ksiazke(ksiazki):
    headers = {"Authorization": f"token {TOKEN}"}
    get_response = requests.get(URL, headers=headers)
    if get_response.status_code == 200:
        sha = get_response.json()["sha"]
    else:
        sha = None
    new_content = base64.b64encode(
        json.dumps(ksiazki, indent = 4, ensure_ascii = False).encode("utf=8")).decode("utf-8")
    data = {
        "message": "Aktualizacja pliku JSON",
        "content": new_content
    }
    if sha:
        data["sha"] = sha

    put_response = requests.put(URL, headers=headers, data=json.dumps(data))

    if put_response.status_code in [200, 201]:
        st.success("Zaktualizowano dane w repozytorium GitHub")
        return True
    else:
        st.error(f"Błąd zapisu: {put_response.status_code}")
        return False