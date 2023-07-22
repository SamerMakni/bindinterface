import streamlit as st
from PIL import Image

def home():
    image = Image.open('./images/Logo_MEEP.png')
    st.image(image, width=400)
