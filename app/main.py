import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import sys
sys.path.append('../app/paginas')
from pagina_inicio import pag_inicio
from pagina_produtos import pag_produtos

st.set_page_config(layout="wide", initial_sidebar_state = 'collapsed', page_title="Ana Medeiros", page_icon=":arrow_down:")

st.markdown("""
    <style>
           #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-vk3wp9.eczjsme11 > div.st-emotion-cache-6qob1r.eczjsme3 > div.st-emotion-cache-16txtl3.eczjsme4{
            padding : 2rem 1.5rem;
            background-color: #000000;
            color: white;
            
           }
        .st-emotion-cache-16txtl3{
            background-color: #000000
        } 
        #root > div:nth-child(1) > div.withScreencast > div > div > div > section.st-emotion-cache-1cypcdb.eczjsme11 > div.st-emotion-cache-6qob1r.eczjsme3 > div.st-emotion-cache-16txtl3.eczjsme4{
            height : 100%}
            
    </style>
""", unsafe_allow_html=True) 

with st.sidebar:

    st.markdown("""
            <div style="background-color: #000000 ;">
            <h1 style="color: white; font-size: 24px;">Menu</h1>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""               
            <style>
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.st-emotion-cache-uf99v8.ea3mdgi8 > div.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 {
                padding : 2rem 1.5rem;
        }
            </style>
    """, unsafe_allow_html=True)


    with stylable_container(
            key="radio_personalizado",
            css_styles=  """
                :first-child>:first-child{
                color: #f0f0f0;
                }
                """,
        ):
            pagina_escolhida = st.radio('Página',['Início', 'Produtos'])

if pagina_escolhida == 'Início':
    pag_inicio()
            
if pagina_escolhida == 'Produtos':
    pag_produtos()
            


 
