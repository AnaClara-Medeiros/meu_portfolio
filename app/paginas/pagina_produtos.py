import streamlit as st
from paginas.dashboards import pag_dashboards
from paginas.automacoes import pag_automacoes
from paginas.github import pag_github
from modulos.get_url_from_png import get_base64_of_png_file


def pag_produtos():
    bin_str = get_base64_of_png_file(r'app/outros/produtos.png') #transformar um arqv local em html

    estilo_pagina = """
    <style>
     [data-testid="stAppViewContainer"] {
     background-image : url("data:image/png;base64,%s");
     background-size : cover;
     }
 
     [data-testid="stHeader"] {
     background-color : rgba(0,0,0,0);
     }

    #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-vk3wp9.eczjsme11 > div.st-emotion-cache-6qob1r.eczjsme3 {
      background-color: #000000;

    </style>"""% bin_str


    st.markdown(estilo_pagina, unsafe_allow_html=True)


    col1, col2, col3 = st.columns([0.33,0.33,0.33])
    with col1:
        st.markdown("<br>" * 8, unsafe_allow_html=True)
        # Centraliza o botão na coluna
        if st.button("Dashboards/ Analytics"):
            st.session_state.pag = 'dashboards'
    
    with col2:
        st.markdown("<br>" * 8, unsafe_allow_html=True)
        # Centraliza o botão na coluna
        if st.button('Automações'):
            st.session_state.pag = 'automacoes'

    with col3:
        st.markdown("<br>" * 8, unsafe_allow_html=True)
        # Centraliza o botão na coluna
        if st.button('Machine Learning'):
            st.session_state.pag = 'machine'

def main_pag_produtos():
    if "pag" not in st.session_state:
        st.session_state.pag = 'produtos'

    if st.session_state.pag == "dashboards":
        pag_dashboards()
    elif st.session_state.pag == "automacoes":
        pag_automacoes()
    elif st.session_state.pag == "machine":
        pag_github()
    else:
        pag_produtos()




       
    
    
    