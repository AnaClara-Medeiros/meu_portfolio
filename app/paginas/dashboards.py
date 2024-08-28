import streamlit as st
import sys
sys.path.append('app//modulos')
from get_url_from_png import get_base64_of_png_file
# Dados dos dashboards do Power BI com suas pré-visualizações

vendas_png = get_base64_of_png_file(r'outros/dash_vendas.png')
financeiro_png = get_base64_of_png_file(r'outros/dash_financeiro.png')
#financas_png = get_base64_of_png_file(r'outros/dash_financas.png')
logistica_png = get_base64_of_png_file(r'outros/dash_logistica.png')

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
st.write("Power BI Dashboards")

# Exibição dos dashboards
for dashboard in dashboards:
    st.subheader(dashboard["title"])
    st.image(dashboard["image"], use_column_width=True)
    st.markdown(f"[Veja o Dashboard]({dashboard['link']})", unsafe_allow_html=True)
