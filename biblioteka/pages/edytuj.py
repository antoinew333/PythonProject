import streamlit as st
import json

def zapisz_ksiazke(ksiazki):
    with open("plik_ksiazki.json", "w", encoding = "utf-8") as plik:
        json.dump(ksiazki, plik, indent = 4, ensure_ascii = False)

def wczytaj_ksiazki():
    try:
        with open("plik_ksiazki.json", "r") as plik:
            return json.load(plik)
    except (FileNotFoundError, json.JSONDecodeError):
        print("FileNotFoundError")
    return []

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