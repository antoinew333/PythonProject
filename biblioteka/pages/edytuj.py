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
    if st.button("Potwierdź"):
        tytul = st.text_input("Tytuł: ", st.text(pozycje[0]))
        autor = st.text_input("Autor: ", st.text(pozycje[1]))
        wydawnictwo = st.text_input("Wydawnictwo: ", st.text(pozycje[2]))
        rok = st.text_input("Rok: ", st.text(pozycje[3]))
        status = st.checkbox("Przeczytana", width="stretch")
        if status == "przeczytana":
            status = True
        elif status == "nieprzeczytana":
            status = False
        if st.button("Zapisz"):
            st.session_state.ksiazki.update({"Tytuł": tytul,
                                             "Autor": autor,
                                             "Wydawnictwo": wydawnictwo,
                                             "Rok": rok,
                                             "Przeczytana": status})
            zapisz_ksiazke(st.session_state.ksiazki)
            st.session_state.edytowanie = False
            st.success("Książka została zedytowana")

st.page_link("main.py", label="Powrót do MENU")