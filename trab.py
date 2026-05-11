import streamlit as st

st.image("Foto-empresa.png")
st.link_image("https://www.starbucks.com.br/")
st.write("Site Clara Ferreira")
st.write("Clara Ferreira")
st.write("Sou estudante do IFPB e, mesmo sem muita experiência, possuo grande vontade de apernder. Escolhi representar a aempresa acima, pois é onde muitos desejam se empregar.")
st.write("Acessar meu site abaixo")
st.link_button("Acessar", "https://sites.google.com/academico.ifpb.edu.br/site-m-clara-ferreira/exerc%C3%ADcios")

import streamlit as st
import base64

# CONFIG
st.set_page_config(page_title="Perfil", layout="wide")

# FUNÇÃO base64
def get_base64_image(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

img_base64 = get_base64_image("star.png")
zap_base64 = get_base64_image("zap2026.png")

# TOPO (imagem clicável)
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 50px;">
            <a href="https://www.starbucks.com.br/" target="_blank">
                <img src="Foto-empresa.png,{img_base64}" 
                     width="320" 
                     style="border-radius:12px;">
            </a>
        </div>
    """, unsafe_allow_html=True)

# LAYOUT PRINCIPAL
col_left, col_right = st.columns([3,1])

with col_left:
    st.markdown("""
    <div style='margin-bottom:30px; font-size:30px;'>
        <b>Nome Maria Clara</b>
    </div>
    """, unsafe_allow_html=True)

    # subcolunas
    subcol1, subcol2 = st.columns([1,4])

    # IMAGEM (centralizada verticalmente)
    with subcol1:
        st.markdown("""
        <div style="
            display: flex;
            align-items: center;
            height: 100%;
        ">
        """, unsafe_allow_html=True)

        st.image("Foto moana.png", width=800)

        st.markdown("</div>", unsafe_allow_html=True)

    # TEXTO
    with subcol2:
        st.markdown("""
        <div style="
            text-align: justify;
            font-size: 20px;
            line-height: 2.0;
            width: 100%;
            max-width: none;
        ">
            <b>Sobre Maria Clara:<br>
            Maria Clara é uma estudante do curso técnico em informática no IFPB campus Itabaiana e é uma leitora muito esforçada.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='margin-top:30px;'>", unsafe_allow_html=True)
    st.link_button("Acessar", "https://sites.google.com/academico.ifpb.edu.br/site-m-clara-ferreira/exerc%C3%ADcios")
    st.markdown("</div>", unsafe_allow_html=True)

with col_right:
    st.empty()

# 🔥 NOVO BLOCO (WhatsApp clicável no final)
st.markdown(f"""
    <div style="text-align: center; margin-top: 10px;">
        <a href="https://web.whatsapp.com/" target="_blank">
            <img src="https://web.whatsapp.com/" width="100">
        </a>
    </div>
""", unsafe_allow_html=True)
