import streamlit as st
from modulos.get_url_from_png import get_base64_of_png_file
from modulos.open_page_url import open_page
import streamlit.components.v1 as components



def pag_apresentacoes():
    bin_str = get_base64_of_png_file(r'app/outros/pag_apresentacoes.png') #transformar um arqv local em html

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

    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        components.iframe("https://www.linkedin.com/feed/update/urn:li:activity:7253035103453364225/", width=600, height=500)
    if col1.button('Palestra Business Inteligence - FATEC Assis'):
        open_page('https://www.linkedin.com/feed/update/urn:li:activity:7253035103453364225/')


    if col2.button('Minicurso - Introdução ao Python'):
        open_page('https://www.youtube.com/playlist?list=PL2lhbF8mjkwioIrekH0JKyCMqDcsFE3if')

    if col3.button('Congresso Ciência de Dados das Fatecs'):
        open_page('https://www.linkedin.com/feed/update/urn:li:activity:6863625691813019648/')