import streamlit as st


def remove_background_image():
    st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {{
            background-image: none;
        }}
    </style>""", unsafe_allow_html=True)


def pag_dashboards():
    remove_background_image()
    st.write('dashboards AQUI')

if __name__ == '__main__':
    pag_dashboards()