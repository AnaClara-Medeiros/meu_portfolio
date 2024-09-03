import streamlit as st
from modulos.open_page_url import open_page



def pag_automacoes():
    open_page('https://github.com/AnaClara-Medeiros')

    if st.button("Voltar para Produtos"):
        st.session_state.pag = 'produtos'

