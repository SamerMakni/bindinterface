from st_on_hover_tabs import on_hover_tabs
import streamlit as st
from search import search
from home import home
st.set_page_config(layout="wide")


def search_tab():
    st.title("Paper")
    st.write('Name of option is Search')

def predict_tab():
    st.title("Tom")
    st.write('Name of option is Predict')

def contact_us_tab():
    st.title("Tom")
    st.write('Name of option is Contact Us')

st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)
hide_streamlit_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

with st.sidebar:
    tabs = on_hover_tabs(tabName=['Home', 'Search', 'Predict', 'Contact Us'], 
                         iconName=['home', 'search', 'batch_prediction', 'contact_page'],
                         key="0")

if tabs == 'Home':
    home()
    """
    ### Molecular Activity Database for Leishmaniasis
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum
    """

elif tabs == 'Search':
    search()

elif tabs == 'Predict':
    predict_tab()

elif tabs == 'Contact Us':
    contact_us_tab()
