import streamlit as st
import sys
sys.path.append('./modulos')
from get_url_from_png import get_base64_of_png_file


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
    
    
if __name__ == '__main__':
    pag_inicio()