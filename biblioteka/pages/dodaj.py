import streamlit as st

from ..data_manager import wczytaj_ksiazki, zapisz_ksiazke

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