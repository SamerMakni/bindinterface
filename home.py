import streamlit as st
from PIL import Image


def home():
    meep = Image.open('./media/Logo_MEEP.png')
    bind = Image.open('./media/logo_BIND.png')
    ipt = Image.open('./media/logo_IPT.png')
    cidals = Image.open('./media/logo_CidalsDB.png')
    all_logos = Image.open('./media/logos.png') 

    cola, colb, colc= st.columns([0.2, 0.6, 0.2])
    with cola:
        pass
    with colb:
        st.image(url="https://i.ibb.co/5Knkk4G/logo-cidals.png", alt="logo-cidals", width=600)
    with colb:
        pass
    st.markdown("""
    CidalsDB is an open resource on anti-pathogen molecules that offers a chemical similarity-based browsing function and an AI-based prediction tool of the 'cidal' effect of chemical compounds against pathogens, such as Leishmania parasites1 and Coronaviruses (SARS-Cov, SARS-Cov-2, MERS)2.

CidalsDB is an evolutive platform for democratized and no-code Computer-Aided Drug Discovery (CADD)3, and we work continuously on including further pathogens, datasets and AI predictive models.

1. Harigua-Souiai, E., Oualha, R., Souiai, O., Abdeljaoued-Tej, I. & Guizani, I. Applied machine learning toward drug discovery enhancement: Leishmaniases as a case study. Bioinforma. Biol. Insights 16, 11779322221090349 (2022).
2. Harigua-Souiai, E. et al. Deep learning algorithms achieved satisfactory predictions when trained on a novel collection of anticoronavirus molecules. Front. Genet. 12, 744170 (2021).
3. Harigua-Souiai, E., Makni, S., Masmoudi, O., Hamdi, S., Oualha, R., Abdelkrim, Y.Z.,Souiai, O., Guizani, I. CidalsDB: An AI-empowered platform for anti-pathogen therapeutics research. Submitted.
    
    
    """)