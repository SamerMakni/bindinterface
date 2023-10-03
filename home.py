import streamlit as st
from PIL import Image


def home():
    meep = Image.open('./media/Logo_MEEP.png')
    bind = Image.open('./media/Logo_BIND.png')
    ipt = Image.open('./media/Logo_IPT.png')

    col1, col2, col3= st.columns([0.2, 0.4, 0.4])
    with col1:
        st.image(bind, width=200)

    with col2:
        st.image(meep, width=400)

    with col3:
        st.image(ipt, width=200)
    st.markdown(r"$$\textrm{\large{CidalsDB and its ML-based activity prediction module present a democratized and no-code CADD tool.}}$$")