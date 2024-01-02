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
        st.image("https://i.ibb.co/5Knkk4G/logo-cidals.png", width=300)
    with colb:
        pass
    with colb:
        pass
    st.markdown(r"""
   
CidalsDB serves as an evolutive platform for democratized and no-code Computer-Aided Drug Discovery (CADD)<sup>3</sup>. We would like to acknowledge the following contributions:

- Harigua-Souiai, E., Oualha, R., Souiai, O., Abdeljaoued-Tej, I. & Guizani, I. (2022). Applied machine learning toward drug discovery enhancement: Leishmaniases as a case study. Bioinforma. Biol. Insights 16, 11779322221090349<sup>1</sup>.

- Harigua-Souiai, E. et al. (2021). Deep learning algorithms achieved satisfactory predictions when trained on a novel collection of anticoronavirus molecules. Front. Genet. 12, 744170<sup>2</sup>.

- Harigua-Souiai, E., Makni, S., Masmoudi, O., Hamdi, S., Oualha, R., Abdelkrim, Y.Z., Souiai, O., Guizani, I. CidalsDB: An AI-empowered platform for anti-pathogen therapeutics research. Submitted<sup>3</sup>.
""")

    