import streamlit as st
from streamlit_extras.stylable_container import stylable_container 
from streamlit_extras.bottom_container import bottom
import sys
sys.path.append('../modulos')
from get_url_from_png import get_base64_of_png_file
from pag_produtos import pag_produtos

def pag_inicio():
    bin_str = get_base64_of_png_file(r'D:\anacl\AnaClara-arqv\Portfolio\app\outros\home.png') #transformar um arqv local em html

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

    col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])

    with col5:
      with stylable_container(
          key="button_produtos",
          css_styles="""
              button {
                  background-color: #c4459f;
                  color: white;
                  border-radius: 20px;
                  border-color: #c4459f;
              }
              """,):

          if st.button('PROJETOS AQUI!'):
             st.session_state.page = "produtos"
             #st.experimental_rerun()
    
if 'page' not in st.session_state:
    st.session_state.page = "inicio"

# Renderiza a página com base no estado atual
if st.session_state.page == "produtos":
    pag_produtos()
elif st.session_state.page == "inicio":
    pag_inicio()
    
    

   
    

