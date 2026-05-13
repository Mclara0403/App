import streamlit as st

col1, col2, col3 = st.columns([1, 2, 3])

with col2:
  st.image("Foto-empresa.png", width=300, link="https://www.starbucks.com.br/")

st.title("Nome: Clara Ferreira")

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
  st.image("foto-clara.jpg", width=300)
 
with col2:
  st.header("Sobre Mim:")
  st.write(" Leitora que insiste em se atriscar na vida e estudante do terceiro ano do curso técnico integrado em informática - campus Itabaiana ")

st.write("")
 
st.link_button("Acessar Site", "https://sites.google.com/academico.ifpb.edu.br/site-m-clara-ferreira/in%C3%ADcio")

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 3])

with col2:
  st.image("download.png", width=100, link="https://wa.me/+5583986246096")
