estilo = '''
    <style>

    .title-text {{
        color: #C4459F;
    }}


    #root > div:nth-child(1) > div.withScreencast > div > div > header{{
            background-color: transparent !important ;
            position: relative; /* Necessário para o z-index funcionar */
            z-index: 0;}}

    .stButton button {{
        background-color: #4F124D;
        color: #ffffff;
        padding: 10px;
        margin: -5px 0;
        border: 1px solid #ffffff;
        border-radius: 20px;
        cursor: pointer;
        width: 100%;
        display: flex;
        justify-content: flex-start;
    }}
    .stButton button:hover {{
        background-color: #C4459F;
        border: 1px solid #C4459F;
        color: #ffffff;
    }}
    </style>
'''