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


    
    st.header("Search")
    st.subheader("a. Sørensen-Dice Coefficient")
    st.write("The Sørensen-Dice coefficient is a measure of the similarity between two sets...")
    st.latex(r"S(Dice) = \frac{2 \cdot |A \cap B|}{|A| + |B|}")
    
    st.subheader("b. Tanimoto Coefficient")
    st.write("The Tanimoto coefficient, also known as the Jaccard index, measures the similarity...")
    st.latex(r"T(Tanimoto) = \frac{|A \cap B|}{|A| + |B| - |A \cap B|}")
    
    st.subheader("c. Cosine Similarity")
    st.write("Cosine similarity is a measure of the cosine of the angle between two vectors...")
    st.latex(r"S(Cosine) = \frac{A \cdot B}{\|A\| \cdot \|B\|}")
    
    st.subheader("d. Tversky Index")
    st.write("The Tversky index is a generalization of the Sørensen-Dice coefficient that...")
    st.latex(r"T(Tversky) = \frac{|A \cap B|}{|A \cap B| + \alpha \cdot |A \backslash B| + \beta \cdot |B \backslash A|}")
    
    st.subheader("e. Average of Scores")
    st.write("To obtain a comprehensive similarity score, the four similarity measures...")
    st.write("The normalized scores are averaged to provide a combined similarity measure.")

    st.header("3. Machine Learning Model")
    st.subheader("Data used for training")
    st.write(text)
    
    st.subheader("Algorithm used")
    st.write(text)