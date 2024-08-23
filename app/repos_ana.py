import streamlit as st
import os
import sys
sys.path.append('../paginas')
from pagina_inicio import pag_inicio
from pagina_produtos import pag_produtos

st.set_page_config(layout='wide', page_title='Ana Medeiros')


# Inicializa o estado da página se não estiver definido
if 'page' not in st.session_state:
    st.session_state.page = "inicio"

# Renderiza a página com base no estado atual
if st.session_state.page == "produtos":
    pag_produtos()
else:
    pag_inicio = import_pag_inicio()
    pag_inicio()




