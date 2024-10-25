import streamlit as st
from modulos.open_page_url import open_page

def pag_github():
    col1, col2, col3, col4 = st.columns(4, gap="medium")
    # Título da página
    col1.write(
        f"""
        <div class="container" style="display: flex; align-items: left; width: 100%; background-color: hashtag#FFFFFF;">
        <div style='background-color: hashtag#ffffff; '>
        <h2 style='text-align: left; color: #ffffff; font-size: 30px;'>Bots</h2>
        <h5 style='text-align: left; color: #ffffff; font-size: 14px;'> É possível automatizar uma ampla variedade de tarefas, desde tarefas simples e repetitivas até tarefas mais complexas e específicas. Imagine poder automatizar a coleta de dados de um site, enviar e-mails personalizados em massa ou até mesmo interagir com APIs de terceiros!</h5>
        </div>
        </div>
        """,
        unsafe_allow_html=True
        )
    
    if col1.button('Ver Bots'):
        open_page('https://github.com/AnaClara-Medeiros/Scraping')

    col2.write(
        f"""
        <div class="container" style="display: flex; align-items: left; width: 100%; background-color: hashtag#FFFFFF;">
        <div style='background-color: hashtag#ffffff; '>
        <h2 style='text-align: left; color: #ffffff; font-size: 30px;'>Sites e Apps</h2>
        <h5 style='text-align: left; color: #ffffff; font-size: 14px;'> Com o auxílio de tecnologias inovadoras e sistemas automatizados, a automatização de processos tem em vista aumentar a eficiência, precisão e produtividade das atividades de uma empresa.</h5>
        </div>
        </div>
        """,
        unsafe_allow_html=True
        )
    
    if col2.button('Ver Sites e Apps'):
        open_page('https://github.com/AnaClara-Medeiros/Scraping')


    # Título da página
    col3.write(
        f"""
        <div class="container" style="display: flex; align-items: left; width: 100%; background-color: hashtag#FFFFFF;">
        <div style='background-color: hashtag#ffffff; '>
        <h2 style='text-align: left; color: #ffffff; font-size: 30px;'>Modelos de Machine Learning</h2>
        <h5 style='text-align: left; color: #ffffff; font-size: 14px;'> Tenha soluções de sistemas que podem aprender com dados, identificar padrões e tomar decisões com o mínimo de intervenção humana.</h5>
        </div>
        </div>
        """,
        unsafe_allow_html=True
        )
    
    if col3.button('Ver Machine Learning'):
        open_page('https://github.com/AnaClara-Medeiros/Machine_learning')

    # Título da página
    col4.write(
        f"""
        <div class="container" style="display: flex; align-items: left; width: 100%; background-color: hashtag#FFFFFF;">
        <div style='background-color: hashtag#ffffff; '>
        <h2 style='text-align: left; color: #ffffff; font-size: 30px;'>WebScraping</h2>
        <h5 style='text-align: left; color: #ffffff; font-size: 14px;'>Por meio dessa técnica, é possível extrair informações dos produtos e dos preços de e-commerces. Uma vez que os dados foram capturados podem ser mensurados e analisados pelas empresas, com o objetivo de avaliar os concorrentes e o mercado.</h5>
        </div>
        </div>
        """,
        unsafe_allow_html=True
        )
    
    if col4.button('Ver WebScraping'):
        open_page('https://github.com/AnaClara-Medeiros/Scraping')