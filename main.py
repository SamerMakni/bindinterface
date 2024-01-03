from st_on_hover_tabs import on_hover_tabs
import streamlit as st
from search import search
from predict import predict
from contact import contact
from home import home
from about import about
import time
from streamlit_extras.app_logo import add_logo

st.set_page_config(
    page_title="CidalsDB",
    page_icon="./media/logo_BIND.ico",
    layout="wide",
)


st.markdown('<style>' + open('./src/style.css').read() + '</style>', unsafe_allow_html=True)
hide_streamlit_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            div.appview-container>section {top: 0px}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
streamlit_style = """
			<style>
            
            @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Display:wght@300&display=swap');
			html, body, [class*="css"]  {
            font-family: 'Noto Sans Display', sans-serif;;
			}
			</style>
			"""
st.markdown(streamlit_style, unsafe_allow_html=True)

with st.sidebar:
    tabs = on_hover_tabs(tabName=['Home', 'Search', 'Predict', 'Contact Us'], 
                         iconName=['home', 'search', 'functions', 'alternate_email'],
                         key="1",
                         default_choice=0)

if tabs == 'Home':
    home()
    about()

elif tabs == 'Search':
    search()

elif tabs == 'Predict':
    predict()

elif tabs == 'Contact Us':
    contact()
