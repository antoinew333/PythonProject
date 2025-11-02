import streamlit as st

st.set_page_config(initial_sidebar_state="collapsed")

st.title(":blue[BIBLIOTEKA]", width="content")

st.image("https://star-wars.pl/grafika/mar2002/jedilib.jpg")

st.page_link("pages/dodaj.py", label="Dodaj ksiązkę", width="content")

st.page_link("pages/wyswietl.py", label="Wyświetl ksiązkę", width="content")

st.page_link("pages/usun.py", label = "Usuń książkę", width="content")