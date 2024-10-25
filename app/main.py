import streamlit as st
import style_config
from streamlit_option_menu import option_menu
from paginas.pagina_inicio import pag_inicio
from paginas.dashboards import pag_dashboards
from paginas.apresentacoes import pag_apresentacoes
from paginas.github import pag_github
from paginas.pagina_produtos import main_pag_produtos


st.set_page_config(layout="wide", initial_sidebar_state = 'collapsed', page_title="Ana Medeiros")

estilo_html_css = style_config.estilo
st.markdown(estilo_html_css, unsafe_allow_html=True) 

selected = option_menu(None, ["Home", "DataViz/Dashboards","IA/Automações", "Apresentações","Certificados"], 
            icons=['house', 'file-bar-graph','robot', 'file-play','file-check'], menu_icon="cast", default_index=0, orientation='horizontal',
            styles={"container": {"padding": "0!important", "background-color": "transparent"}})

if selected == 'Home':
    pag_inicio()
            
if selected == 'DataViz/Dashboards':
    st.session_state.pag = 'dashboards'
    pag_dashboards()

if selected == 'IA/Automações':
    st.session_state.pag = 'github'
    pag_github()
            
if selected == 'Apresentações':
    st.session_state.pag = 'apresentacao'
    pag_apresentacoes()

 
