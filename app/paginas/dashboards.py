import streamlit as st
from modulos.get_url_from_png import get_base64_of_png_file
# Dados dos dashboards do Power BI com suas pré-visualizações

def pag_dashboards():

    vendas_png = r'app/outros/dash_vendas.png'
    financeiro_png = r'app/outros/dash_financeiro.png'
    #financas_png = r'app/app/outros/dash_financas.png')    
    logistica_png = r'app/outros/dash_logistica.png'

    dashboards = [
        {
            "title": "Dashboard de Vendas",
            "link": "https://app.powerbi.com/view?r=eyJrIjoiOTg2ZWVlMjAtZTYyZi00MjA2LTllMzUtYjM4MjRkNWU3NDg2IiwidCI6IjAzYmI2NTdmLTVmOWQtNDEyZi04Yjg1LWIzNmQ0NzJiZWMyMCJ9",
            "image": f"{vendas_png}"
        },
        {
            "title": "Dashboard de Logistica",
            "link": "https://app.powerbi.com/view?r=eyJrIjoiMDY2ZThmYzEtMDc2NC00MmU1LWJjYjEtMTk5M2MxMTdjMjk4IiwidCI6IjAzYmI2NTdmLTVmOWQtNDEyZi04Yjg1LWIzNmQ0NzJiZWMyMCJ9",
            "image": f"{logistica_png}"
        },
        {
            "title": "Dashboard Financeiro",
            "link": "https://app.powerbi.com/view?r=eyJrIjoiOTlmMDljNzMtZjJlMy00OGZiLWI5ZWUtYzlmMTRhNzk5ZmI2IiwidCI6IjAzYmI2NTdmLTVmOWQtNDEyZi04Yjg1LWIzNmQ0NzJiZWMyMCJ9",
            "image": f"{financeiro_png}"
        }

    ]

    # Título da página
    st.write(
        f"""
        <div class="container" style="display: flex; align-items: left; width: 100%; background-color: hashtag#FFFFFF;">
        <div style='background-color: hashtag#ffffff; '>
        <h1 style='text-align: left; color: #ffffff; font-size: 40px;'>Power BI Dashboards</h1>
        <h3 style='text-align: left; color: #ffffff; font-size: 18px;'>Tenha uma ferramenta gráfica que reúne informações relevantes do seu negócio, dados de desempenho, métricas de KPI e muito mais para ver os resultados de uma única vez.</h3>
        </div>
        </div>
        """,
        unsafe_allow_html=True
        )
    # Exibição dos dashboards
    for dashboard in dashboards:
        st.subheader(dashboard["title"])
        st.markdown(f"[Veja o Dashboard]({dashboard['link']})", unsafe_allow_html=True)
        st.image(dashboard["image"], use_column_width=True)
        
