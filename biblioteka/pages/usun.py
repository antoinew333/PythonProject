import streamlit as st
import json

def zapisz_ksiazke(ksiazki):
    plik = open("ksiazki.json", "w")
    json.dump(ksiazki, plik, indent = 2)
    plik.close()

def wczytaj_ksiazki():
    try:
        with open("ksiazki.json", "r") as plik:
            ksiazki = json.load(plik)
    except (FileNotFoundError, json.JSONDecodeError):
        print("FileNotFoundError")
        ksiazki = []
    return ksiazki

st.set_page_config(initial_sidebar_state="collapsed")

if "ksiazki" not in st.session_state:
    st.session_state.ksiazki = wczytaj_ksiazki()

if "usuwanie" not in st.session_state:
    st.session_state["usuwanie"] = False

st.session_state["usuwanie"] = True
pozycje = [x["Tytuł"] for x in st.session_state.ksiazki]
usun = st.selectbox("Wybierz książkę do usunięcia: ", options=pozycje)
if st.button("Potwierdź"):
    st.session_state.ksiazki = [x for x in st.session_state.ksiazki if x["Tytuł"] != usun]
    zapisz_ksiazke(st.session_state.ksiazki)
    st.success("Książka została usunięta")

st.page_link("main.py", label="Powrót do MENU")