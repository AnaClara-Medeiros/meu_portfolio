import streamlit as st
from streamlit_extras.stylable_container import stylable_container 
from dashboards import pag_dashboards
from automacoes import pag_automacoes
from github import pag_github
import sys
sys.path.append('./app/modulos')
from get_url_from_png import get_base64_of_png_file


def pag_produtos():
    bin_str = get_base64_of_png_file(r'D:\anacl\AnaClara-arqv\Portfolio\app\outros\produtos.png') #transformar um arqv local em html

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
    with col3:
        with stylable_container(
          key="button_dash",
          css_styles="""
              button {
                  background-color: #c4459f;
                  color: white;
                  border-radius: 20px;
                  border-color: #c4459f;
                  position: fixed; /* Fixa o botão na tela */
                  bottom: 20px; /* Distância do canto inferior */
                  right: 230px;
              }
              """,):

          if st.button('Abrir'):
             st.session_state.pagina = "dashboards"
    
if 'pagina' not in st.session_state:
    st.session_state.pagina = "produtos"

# Renderiza a página com base no estado atual
if st.session_state.pagina == "dashboards":
    pag_dashboards()
elif st.session_state.pagina == "automacoes":
    pag_automacoes()
elif st.session_state.pagina == "github":
    pag_github()
elif st.session_state.pagina == "produtos":
    pag_produtos()

    
    
    