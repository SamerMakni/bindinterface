import streamlit as st
from lorem_text import lorem

text = lorem.paragraph()
def about():
    st.title("About")
    st.header("1. Data")
    st.write(text)
    
    st.header("2. Search")
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