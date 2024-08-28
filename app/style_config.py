#cores
branco = "#ffffff"
roxo_escuro = "4F124D"
roxo_claro = "C4459F"

# Estilo customizado para botões
estilo = f'''
    <style>
    
    .title-text {{
        color: {roxo_claro}
    }}

    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 {{
        padding : 0.5rem 5rem;
    }}

    #root > div:nth-child(1) > div.withScreencast > div > div > header{{
        background-color: transparent ;
        position: relative; /* Necessário para o z-index funcionar */
        z-index: 0;}}

    .menu {{
        background-color: transparent ;
    }}

    .st-emotion-cache-6qob1r {{
        background-color: {roxo_escuro} !important;
    }}
    .stButton button {{
        background-color: {roxo_escuro};
        color: {branco};
        padding: 10px;
        margin: -5px 0;
        border: 1px solid {branco};
        border-radius: 20px;
        cursor: pointer;
        width: 100%;
        display: flex;
        justify-content: flex-start;
    }}
    .stButton button:hover {{
        background-color: {roxo_claro};
        border: 1px solid {roxo_claro};
        color: {branco};
    }}
    </style>
    '''