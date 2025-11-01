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

if "edytowanie" not in st.session_state:
    st.session_state["edytowanie"] = False

st.session_state["edytowanie"] = True

pozycje = [x["Tytuł"] for x in st.session_state.ksiazki]
edycja = st.selectbox("Wybierz książkę do edytowania: ", options=pozycje)

if st.session_state["edytowanie"]:
    tytul = st.text_input("Tytuł: ", pozycje["Tytuł"])
    autor = st.text_input("Autor: ", pozycje["Autor"])
    wydawnictwo = st.text_input("Wydawnictwo: ", pozycje["Wydawnictwo"])
    rok = st.text_input("Rok: ", pozycje.get("Rok", ""))
    status = st.checkbox("Przeczytana", value=pozycje.get("Przeczytana", False))
    if status == "przeczytana":
        status = True
    elif status == "nieprzeczytana":
        status = False

    if st.button("Zapisz"):
        pozycje["Tytuł"] = tytul
        pozycje["Autor"] = autor
        pozycje["Wydawnictwo"] = wydawnictwo
        pozycje["Rok"] = rok
        pozycje["Przeczytana"] = status
        zapisz_ksiazke(st.session_state.ksiazki)
        st.session_state.edytowanie = False
        st.success("Książka została zedytowana")

st.page_link("main.py", label="Powrót do MENU")