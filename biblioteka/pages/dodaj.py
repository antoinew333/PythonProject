import streamlit as st
import json

def zapisz_ksiazke(ksiazki):
    with open("plik_ksiazki.json", "w", encoding="utf-8") as plik:
        json.dump(ksiazki, plik, indent=4, ensure_ascii=False)

def wczytaj_ksiazki():
    try:
        with open("plik_ksiazki.json", "r", encoding="utf-8") as plik:
            return json.load(plik)
    except (FileNotFoundError, json.JSONDecodeError):
        print("FileNotFoundError")
        return []


st.set_page_config(initial_sidebar_state="collapsed")

if "ksiazki" not in st.session_state:
    st.session_state.ksiazki = wczytaj_ksiazki()

if "dodawanie" not in st.session_state:
    st.session_state.dodawanie = False

st.session_state.dodawanie= True

if st.session_state.dodawanie:
    tytul = st.text_input("Tytuł: ")
    autor = st.text_input("Autor: ")
    wydawnictwo = st.text_input("Wydawnictwo: ")
    rok = st.text_input("Rok: ")
    status = st.checkbox("Przeczytana")

    if st.button("Zapisz książkę"):
        if len(tytul) != 0:
            st.session_state.ksiazki.append({"Tytuł": tytul,
                                             "Autor": autor,
                                             "Wydawnictwo": wydawnictwo,
                                             "Rok": rok,
                                             "Przeczytana": status})
            zapisz_ksiazke(st.session_state.ksiazki)
            st.session_state.dodawanie = False
            st.success("Książka została dodana do biblioteki")
        else:
            st.warning("Uzupełnij puste pola")


st.page_link("main.py", label="Powrót do MENU")