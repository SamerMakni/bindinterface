import streamlit as st
from PIL import Image

def home():
    image = Image.open('./media/Logo_MEEP.png')
    st.image(image, width=400)
