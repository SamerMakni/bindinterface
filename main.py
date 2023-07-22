from st_on_hover_tabs import on_hover_tabs
import streamlit as st
from search import search
from predict import predict
from contact import contact
from home import home
from about import about
import time
from streamlit_extras.app_logo import add_logo


st.set_page_config(layout="wide")
add_logo("http://placekitten.com/120/120")


st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)
hide_streamlit_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            div.appview-container>section {top: 0px}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# Set 'Home' as the default tab


with st.sidebar:
    tabs = on_hover_tabs(tabName=['Home', 'About','Search', 'Predict', 'Contact Us'], 
                         iconName=['home', 'info','search', 'functions', 'alternate_email'],
                         key="1",
                         default_choice=0)



if tabs == 'Home':
    home()
    
elif tabs == 'About':
    about()

elif tabs == 'Search':
    search()

elif tabs == 'Predict':
    predict()

elif tabs == 'Contact Us':
    contact()