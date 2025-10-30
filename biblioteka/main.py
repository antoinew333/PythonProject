import streamlit as st
import json

def wczytaj_ksiazki():
    try:
        with open("ksiazki.json", "r") as plik:
            ksiazki = json.load(plik)
    except (FileNotFoundError, json.JSONDecodeError):
        print("FileNotFoundError")
        ksiazki = []
    return ksiazki

st.set_page_config(initial_sidebar_state="collapsed")

st.title(":blue[BIBLIOTEKA]", width="content")

st.page_link("pages/dodaj.py", label="Dodaj książkę", width="stretch")

st.page_link("pages/wyswietl.py", label="Wyświetl ksiązkę", width="stretch")

st.page_link("pages/usun.py", label = "Usuń książkę", width="stretch")