import streamlit as st
from lorem_text import lorem
import plotly.express as px
import pandas as pd
from graphics.figures import *
import base64
from PIL import Image

df = pd.read_csv("./data/cidals_user_view.csv")

text = lorem.paragraph()
meep = Image.open('./media/Logo_MEEP.png')
bind = Image.open('./media/logo_BIND.png')
ipt = Image.open('./media/logo_IPT.png')

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
    """)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(r"""
            #### Tanimoto
    Tanimoto distance is a simple yet powerful metric. It is defined as the ratio of the intersection of the sets to the union of the sets.

    $$
    T = \frac{|A \cap B|}{|A|  +  |B| - |A \cap B|}
    $$

        """)
    with col2:
        st.markdown(r"""
            #### Sørensen-Dice Coefficient
    The Dice distance, also known as the Dice coefficient. It is closely related to the Tanimoto coefficient and quantifies the degree of overlap between two sets of molecular features.

    $$
    D = \frac{2 \cdot |A \cap B|}{|A|  +  |B|}
    $$

        """)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(r"""
            #### Cosine
            Cosine similarity is a common measure of similarity between two vectors. It is calculated by taking the cosine of the angle between the vectors.

            $$
            C = \frac{A \cdot B}{\|A\|  \cdot \|B\|}
            $$
                """)


    with col2:
        st.markdown(r""" 
            #### Tversky
        Tversky is a measure of dissimilarity between two molecular fingerprints.

        $$
        T_2 = \frac{|A \cap B|}{|A \cap B|  +  \alpha \cdot |A \backslash B|  + \beta \cdot |B \backslash A|}
        $$

        """)

    st.markdown(r"""## Workflow""")
    first_co, _ ,last_co = st.columns([0.5,0.1,0.4])
    with last_co:
        st.image("https://i.ibb.co/H71JzVd/search-2-drawio.png", output_format = "png", caption="Pipeline of Chemcial Search", width=300)
    with first_co:
        st.markdown(r"""
            The chemical search feature works by first having the user submit a SMILES query. This query is then converted into a fingerprint. Subsequently, the fingerprint is compared to the fingerprints of all the molecules in the dataset. Using one of the distance measures introduced earlier, it calculates the similarity between the query molecule and each of the molecules in the dataset. Finally, the N (<100) most similar molecules are returned to the user.
            """)
    st.markdown(r"""        
            ## Activity Prediction

            ### Encoding
            The process of data encoding involves transforming the SMILES representations from our molecule dataset into molecular fingerprints. This transformation allows us to extract features from each molecule and represent them in a suitable manner for machine learning algorithms.
            We opted to use [RDKitDescriptors](https://www.rdkit.org/docs/source/rdkit.Chem.Descriptors.html), which are binary vectors with a size we determined to be 2048.

            ### Predictive models
            We trained and optimized ML and DL algorithms on the content of the CidalsDB, namely the RF model on the Leishmania dataset and the GCN model on the Coronaviruses dataset.

            The dataset used for Leishmania is a BioAssay available on [PubChem](https://pubchem.ncbi.nlm.nih.gov/bioassay/1063)(Leishmania major promastigote HTS).  Our approach to data splitting is the 80/20 split, where the dataset is divided into an 80\% training set 
            $$ D_{train} $$  and a 20\%  test set $$ D_{test} $$ , $$len(D_{train}) = 156,938 $$ and  $$len(D_{test}) = 39,235 $$
            To address the problem of class imbalance present in our dataset, we applied Random Oversampling to the training set, changing the ratio between the two classes from 1:9 to 1:1.""")


    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image("https://i.ibb.co/9Y8ppQ6/model-ml-drawio.png", output_format = "png", caption="Pipeline of Traning and Predictions", width=550)
    


    st.markdown(r"""
    ## Acknowledgement
    """)

    cola, colb, colc= st.columns(3)
    with cola:
        st.image(bind, width=300)
    with colb:
        st.image(meep, width=300)
    with colb:
        st.image(ipt, width=300)

    st.markdown(r"""
    ### References
    
[^1^]: Harigua-Souiai, E., Oualha, R., Souiai, O., Abdeljaoued-Tej, I. & Guizani, I. (2022). Applied machine learning toward drug discovery enhancement: Leishmaniases as a case study. Bioinforma. Biol. Insights 16, 11779322221090349.

[^2^]: Harigua-Souiai, E. et al. (2021). Deep learning algorithms achieved satisfactory predictions when trained on a novel collection of anticoronavirus molecules. Front. Genet. 12, 744170.

[^3^]: Harigua-Souiai, E., Makni, S., Masmoudi, O., Hamdi, S., Oualha, R., Abdelkrim, Y.Z., Souiai, O., Guizani, I. CidalsDB: An AI-empowered platform for anti-pathogen therapeutics research. Submitted.
    
                """)
    
    
    