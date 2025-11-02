import streamlit as st
import json
import pandas as pd

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

st.markdown("Lista książek:")

if len(st.session_state.ksiazki) > 0:
    x = pd.DataFrame(st.session_state.ksiazki)
    x.index = range(1, len(x) + 1)
    st.dataframe(x, use_container_width=True)
else:
    st.info("Brak książek w bibliotece.")

st.page_link("pages/edytuj.py", label="Edytuj listę")

st.page_link("main.py", label="Powrót do MENU")