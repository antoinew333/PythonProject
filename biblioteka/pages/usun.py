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