import streamlit as st
import json
import os

sciezka_pliku = os.path.join(os.path.dirname(__file__), "..", "plik_ksiazki.json")
sciezka_pliku = os.path.abspath(sciezka_pliku)

def zapisz_ksiazke(ksiazki):
    with open(sciezka_pliku, "w", encoding = "utf-8") as plik:
        json.dump(ksiazki, plik, indent = 4, ensure_ascii = False)

def wczytaj_ksiazki():
    try:
        with open(sciezka_pliku, "r", encoding = "utf-8") as plik:
            return json.load(plik)
    except (FileNotFoundError, json.JSONDecodeError):
        print("FileNotFoundError")
    return []

st.set_page_config(initial_sidebar_state="collapsed")

if "ksiazki" not in st.session_state:
    st.session_state.ksiazki = wczytaj_ksiazki()

if "usuwanie" not in st.session_state:
    st.session_state.usuwanie = False

st.session_state.usuwanie = True

pozycje = [x["Tytuł"] for x in st.session_state.ksiazki]
usun = st.selectbox("Wybierz książkę do usunięcia: ", options=pozycje)

if st.button("Potwierdź"):
    st.session_state.ksiazki = [x for x in st.session_state.ksiazki if x["Tytuł"] != usun]
    zapisz_ksiazke(st.session_state.ksiazki)
    st.success("Książka została usunięta")

st.page_link("main.py", label="Powrót do MENU")