import streamlit as st
from lorem_text import lorem
import plotly.express as px
import pandas as pd
from graphics.figures import *

df = pd.read_csv("./data/cidals_user_view.csv")

text = lorem.paragraph()
def about():
    st.title("About CidalsDB")
    st.header("Datasets")
    st.write("""
    For now, we have datasets for two infectious diseases of interest within the **CidalsDB** database, that are accessible for the scientific community, namely *Leishmaniases* and *Coronaviruses*. For each disease, we performed an extensive search of the literature and retrieved data on molecules with validated anti-pathogen effects. We defined a data dictionary of published information related to the biological activity of the chemical compounds and used it to build the database. Then, we enriched the literature data with confirmatory screening datasets from PubChem. This led to consolidated sets of active and inactive molecules against Leishmania parasites and Coronaviruses. Additional infectious diseases will be considered to expand the database content.
    """)
    col1, col2 = st.columns(2)
    with col1:
        pie_plot = pie() 
        st.plotly_chart(pie_plot)


    with col2:
        bar_plot = bar()
        st.plotly_chart(bar_plot)


    
    st.markdown(r"""
    ## Chemical Similarity Search
    ### Overview
    Chemical similarity search uses distance measures to assess the similarity or dissimilarity between compounds. These measures help evaluate how different two compounds are from each other, based on their binary fingerprint representation. They are important in the context of matching, searching, and classifying chemical information.
    ### Distance measures
    Different distance measures are used to compare the compounds, such as 

    #### Tanimoto
    Tanimoto distance is a simple yet powerful metric. It is defined as the ratio of the intersection of the sets to the union of the sets.

    $$
    T = \frac{|A \cap B|}{|A|  +  |B| - |A \cap B|}
    $$

    #### Sørensen-Dice Coefficient
    The Dice distance, also known as the Dice coefficient. It is closely related to the Tanimoto coefficient and quantifies the degree of overlap between two sets of molecular features.

    $$
    D = \frac{2 \cdot |A \cap B|}{|A|  +  |B|}
    $$

    #### Cosine
    Cosine similarity is a common measure of similarity between two vectors. It is calculated by taking the cosine of the angle between the vectors.

    $$
    C = \frac{A \cdot B}{\|A\|  \cdot \|B\|}
    $$

    #### Tversky
    Tversky is a measure of dissimilarity between two molecular fingerprints.

    $$
    T_2 = \frac{|A \cap B|}{|A \cap B|  +  \alpha \cdot |A \backslash B|  + \beta \cdot |B \backslash A|}
    $$

    ### How it works
        """)