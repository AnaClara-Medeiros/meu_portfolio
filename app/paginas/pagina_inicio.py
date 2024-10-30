import streamlit as st
from modulos.get_url_from_png import get_base64_of_png_file


def pag_inicio():
    # Carregando as duas imagens
    bin_str1 = get_base64_of_png_file(r'app/outros/home1.png')  # Primeira imagem
    bin_str2 = get_base64_of_png_file(r'app/outros/home2.png')  # Segunda imagem

    estilo_pagina = f"""
    <style>
        html, body {{
            margin: 0;
            padding: 0;
            overflow: hidden; /* Oculta a rolagem se não for necessária */
            height: 100%;
        }}

        .container {{
            display: flex;
            flex-direction: column; /* Coloca as imagens uma embaixo da outra */
            height: 100%; /* Preenche a altura total da tela */
            width: 100%; /* Preenche a largura total da tela */
        }}

        .image {{
            width: 100%; /* Largura da imagem igual à largura da tela */
            height: 100vh; /* Altura da imagem igual à altura da viewport */
            object-fit: cover; /* Ajusta a imagem para cobrir o espaço sem distorção */
            display: block; /* Remove o espaço embaixo da imagem */
        }}

        /* Remove bordas de qualquer elemento */
        * {{
            box-sizing: border-box;
        }}
    </style>
    """

    st.markdown(estilo_pagina, unsafe_allow_html=True)

    # Adicionando as imagens
    st.markdown(f"""
    <div class="container">
        <img src="data:image/png;base64,{bin_str1}" class="image">
        <img src="data:image/png;base64,{bin_str2}" class="image">
    </div>
    """, unsafe_allow_html=True)

    
    
if __name__ == '__main__':
    pag_inicio()