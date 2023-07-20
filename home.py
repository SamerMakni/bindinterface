import streamlit as st
from PIL import Image
def home():
    image = Image.open('./Logo_MEEP.png')
    st.image(image, width=400)
