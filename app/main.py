import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(layout="wide", initial_sidebar_state = 'collapsed', page_title="Ana Medeiros")
from paginas.pagina_inicio import pag_inicio
from paginas.pagina_produtos import main_pag_produtos
from modulos.style_config import estilo

st.markdown(estilo, unsafe_allow_html=True) 

with st.sidebar:
    selected = option_menu(None, ["Home", 'Produtos'], 
            icons=['house', 'robot'], menu_icon="cast", default_index=0)

if selected == 'Home':
    pag_inicio()
            
if selected == 'Produtos':
    st.session_state.pag = 'produtos'
    main_pag_produtos()
            


 
