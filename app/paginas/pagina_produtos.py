import streamlit as st
from dashboards import pag_dashboards
from automacoes import pag_automacoes
from github import pag_github
from modulos.get_url_from_png import get_base64_of_png_file


def pag_produtos():
    bin_str = get_base64_of_png_file(r'outros/produtos.png') #transformar um arqv local em html

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

    st.markdown("""
    <style>
        .custom-button {
            background-color: #4F124D;
            text-color: white;
            text-align: center;
            border-radius: 30px;
            border: 2px solid #c4459f;
            width: 200px;
            padding: 10px;
            font-size: 16px;
            display: inline-block; /* Faz com que o botão se comporte como um bloco inline */
            margin: 0 auto; /* Centraliza o botão horizontalmente */
            box-sizing: border-box; /* Inclui o padding e a borda na largura total */
            text-decoration: none; /* Remove o sublinhado padrão dos links */
        }
    </style>""", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([0.33,0.33,0.33])
    with col1:
        st.markdown("<br>" * 12, unsafe_allow_html=True)
        # Centraliza o botão na coluna
        if st.button("Dashboards/ Analytics"):
            st.session_state.pag = 'dashboards'
    
    with col2:
        st.markdown("<br>" * 12, unsafe_allow_html=True)
        # Centraliza o botão na coluna
        if st.button('Automações'):
            st.session_state.pag = 'automacoes'

    with col3:
        st.markdown("<br>" * 12, unsafe_allow_html=True)
        # Centraliza o botão na coluna
        if st.button('Machine Learning'):
            st.session_state.pag = 'machine'

    if "pag" not in st.session_state:
        st.session_state.pag = 'produtos'

    if st.session_state.pag == "dashboards":
        pag_dashboards()
    elif st.session_state.pag == "automacoes":
        pag_automacoes()
    elif st.session_state.pag == "machine":
        pag_github()



       
    
    
    