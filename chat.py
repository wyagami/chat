import requests
import json
import streamlit as st
from PIL import Image

imagem = Image.open("Cebolinha.png")

with st.sidebar:
#    st.title("Converse com o Cebolinha")
    st.image(imagem, width=100)
    st.sidebar.header("Converse com o Cebolinha")
    st.sidebar.write("""
    - Caso tenha alguma idéia para publicarmos, envie uma mensagem para: 11-990000425 (Willian)
    - Contribua com qualquer valor para mantermos a pagina no ar. PIX (wpyagami@gmail.com)
    """)


def cebolinha_fala(texto):
    """Função para adaptar a fala do Cebolinha, trocando R por L."""
    return texto.replace("r", "l").replace("R", "L")


user_input = st.text_input("Fale com o Cebolinha:")

cebolinha_persona = """
A paltil de agola você é o Cebolinha, um menininho de 7 anos muito inteligente e astuto, 
que sempre bolando planos infalíveis para pegar o Sansão, o coelhinho de pelúcia da Mônica. 
Você fala de um jeito englaçado, tlopcando o 'R' pelo 'L'. Você é muito amigo do Cascão e adola desafial a Mônica, 
mas no fundo gosta dela como amiga. Você é espelto, engenhoso e adola contal histólias!
Responta sempre como o Cebolinha, com humol e divesão!
Responda somente assuntos relacionados com o personagem, nada mais."""

if user_input:
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer " + st.secrets["qwen_key"],
            "Content-Type": "application/json",
            "HTTP-Referer": "<YOUR_SITE_URL>",  # Opcional
            "X-Title": "<YOUR_SITE_NAME>",  # Opcional
        },
        data=json.dumps({
            "model": "qwen/qwen2.5-vl-72b-instruct:free",
            "messages": [
                    {"role": "system", "content": cebolinha_persona},
                    {"role": "user", "content": user_input},            ],
        })
    )
    
    if response.status_code == 200:
        resposta = json.loads(response.content).get("choices", [{}])[0].get("message", {}).get("content", "Eita! Num consegui pensal em nada!")
        st.write(cebolinha_fala(resposta))
    else:
        st.write("Eita! Algo deu enlhado, tenta de novo!")
