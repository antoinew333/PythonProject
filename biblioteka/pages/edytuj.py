import requests
import json
import base64
import streamlit as st


TOKEN = st.secrets["GITHUB_TOKEN"]
FILE_PATH = "plik_ksiazki.json"
GITHUB_REPO = "biblioteka"
GITHUB_USER = "antoinew333"
URL = f"https://api.github.com/repos/antoinew333/biblioteka/contents/plik_ksiazki.json"

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
    sha = get_response.json().get("sha")
    content_encoded = base64.b64encode(
        json.dumps(ksiazki, indent = 4, ensure_ascii = False).encode("utf=8")).decode("utf-8")
    data = {
        "message": "Aktualizacja pliku JSON",
        "content": content_encoded,
        "sha": sha
    }

    put_response = requests.put(URL, headers=headers, data=json.dumps(data))

    if put_response.status_code in [200, 201]:
        st.success("Zaktualizowano dane w repozytorium GitHub")
        return True
    else:
        st.error(f"Błąd zapisu: {put_response.status_code}")
        return False

st.set_page_config(initial_sidebar_state="collapsed")

if "ksiazki" not in st.session_state:
    st.session_state.ksiazki = wczytaj_ksiazki()

if "edytowanie" not in st.session_state:
    st.session_state.edytowanie = False

st.session_state.edytowanie = True

pozycje = [x["Tytuł"] for x in st.session_state.ksiazki]
edycja = st.selectbox("Wybierz książkę do edytowania: ", options=pozycje)

ksiazka = next((x for x in st.session_state.ksiazki if x["Tytuł"] == edycja), None)

if st.session_state.edytowanie:
    tytul = st.text_input("Tytuł: ", ksiazka["Tytuł"])
    autor = st.text_input("Autor: ", ksiazka["Autor"])
    wydawnictwo = st.text_input("Wydawnictwo: ", ksiazka["Wydawnictwo"])
    rok = st.text_input("Rok: ", ksiazka.get("Rok", ""))
    status = st.checkbox("Przeczytana", value=ksiazka.get("Przeczytana", False))
    if status == "przeczytana":
        status = True
    elif status == "nieprzeczytana":
        status = False

    if st.button("Zapisz"):
        ksiazka["Tytuł"] = tytul
        ksiazka["Autor"] = autor
        ksiazka["Wydawnictwo"] = wydawnictwo
        ksiazka["Rok"] = rok
        ksiazka["Przeczytana"] = status
        zapisz_ksiazke(st.session_state.ksiazki)
        st.session_state.edytowanie = False
        st.success("Książka została zedytowana")

st.page_link("main.py", label="Powrót do MENU")