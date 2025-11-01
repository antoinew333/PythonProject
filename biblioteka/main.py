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

def zapisz_ksiazke(ksiazki):
    plik = open("ksiazki.json", "w")
    json.dump(ksiazki, plik, indent = 2)
    plik.close()

st.set_page_config(initial_sidebar_state="collapsed")

st.title(":blue[BIBLIOTEKA]", width="content")

if "ksiazki" not in st.session_state:
    st.session_state.ksiazki = wczytaj_ksiazki()

if "dodawanie" not in st.session_state:
    st.session_state.dodawanie = False

@st.dialog("Dodaj książkę")
def ksiazka():
    if st.session_state["dodawanie"]:
        tytul = st.text_input("Tytuł: ", key="tytul_input")
        autor = st.text_input("Autor: ", key="autor_input")
        wydawnictwo = st.text_input("Wydawnictwo: ", key="wydawnictwo_input")
        rok = st.text_input("Rok: ", key="rok_input")
        status = st.checkbox("Przeczytana", key="status_input")
        if status == "przeczytana":
            status = True
        elif status == "nieprzeczytana":
            status = False

        if st.button("Zapisz książkę"):
            if len(tytul) != 0:
                st.session_state.ksiazki.append({"Tytuł": tytul,
                                                "Autor": autor,
                                                "Wydawnictwo": wydawnictwo,
                                                "Rok": rok,
                                                "Przeczytana": status})
                zapisz_ksiazke(st.session_state.ksiazki)
                st.session_state["dodawanie"] = False
                st.success("Książka została dodana do biblioteki")

                st.session_state.tytul_input = ""
                st.session_state.autor_input = ""
                st.session_state.wydawnictwo_input = ""
                st.session_state.rok_input = ""
                st.session_state.przeczytane_input = False
            else:
                st.warning("Uzupełnij puste pola")

if st.button("Dodaj książkę"):
    st.session_state["dodawanie"] = True
    ksiazka()

st.page_link("pages/wyswietl.py", label="Wyświetl ksiązkę", width="content")

st.page_link("pages/usun.py", label = "Usuń książkę", width="content")