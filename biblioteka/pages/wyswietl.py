import streamlit as st
import json
from numpy.random import default_rng as rng

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
st.dataframe(st.session_state.ksiazki, rng(0).standard_normal((0,0)))

st.page_link("main.py", label="Powrót do MENU")