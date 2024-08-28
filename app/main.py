import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(layout="wide", initial_sidebar_state = 'collapsed', page_title="Ana Medeiros", page_icon=":arrow_down:")
import sys
sys.path.append('app/paginas')
from pagina_inicio import pag_inicio
from pagina_produtos import pag_produtos
import style_config

st.markdown(style_config.estilo, unsafe_allow_html=True) 

with st.sidebar:
    selected = option_menu(None, ["Home", 'Produtos'], 
            icons=['house', 'robot'], menu_icon="cast", default_index=0)

if selected == 'Home':
    pag_inicio()
            
if selected == 'Produtos':
    pag_produtos()
            


 
