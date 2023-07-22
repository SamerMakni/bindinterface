
import streamlit as st
from stmol import showmol
import py3Dmol
from rdkit.Chem import Draw
from rdkit import Chem
from rdkit.Chem import AllChem
import pubchempy
import rdkit.Chem.Descriptors as cd
import rdkit.Chem.Lipinski as lip
from rdkit import Chem
from rdkit.Chem import Descriptors
import numpy as np
from scipy.spatial import distance
import pubchempy as pcp
from PIL import Image
import pickle
import pandas as pd
from streamlit_extras.add_vertical_space import add_vertical_space


def pubchem_id_to_smiles(pubchem_id):
    try:
        compound = pcp.get_compounds(pubchem_id)[0]
        smiles = compound.canonical_smiles
        return smiles
    except (IndexError, pcp.PubChemHTTPError) as e:
        print(f"Error retrieving SMILES for PubChem ID {pubchem_id}: {str(e)}")
        return None

def calculate_distance(smiles, fingerprint_array):
    molecule = Chem.MolFromSmiles(smiles)
    fingerprint = np.array(AllChem.RDKFingerprint(molecule, fpSize=1024))
    distances = distance.cdist(fingerprint.reshape(-1,1), fingerprint_array.reshape(-1,1), 'hamming')
    
    return distances.mean()


def passes_lipinski_rule(smiles):
    molecule = Chem.MolFromSmiles(smiles)
    molecular_weight = Descriptors.MolWt(molecule)
    logp = Descriptors.MolLogP(molecule)
    hbd = Descriptors.NumHDonors(molecule)
    hba = Descriptors.NumHAcceptors(molecule)
    
    if molecular_weight > 500 or logp > 5 or hbd > 5 or hba > 10:
        return False
    else:
        return True


def makeblock(smi):
    mol = Chem.MolFromSmiles(smi)
    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol)
    mblock = Chem.MolToMolBlock(mol)
    return mblock

def render_mol(xyz):
    xyzview = py3Dmol.view()#(width=400,height=400)
    xyzview.addModel(xyz,'mol')
    xyzview.setStyle({'stick':{}})
    xyzview.setBackgroundColor('white')
    xyzview.zoomTo()
    showmol(xyzview,height=400,width=800)

def generate_name(smiles):
    compounds = pubchempy.get_compounds(smiles, namespace='smiles')
    match = compounds[0]
    return match.iupac_name

def distance(smile1, smile2):
    """
    Placeholder for the distance function.
    This function should return a value between 0 and 1.
    """
    return np.random.rand()

def highlight_active(val):
    if val == 'Active':
        return 'color: green; font-weight: 800'
    else:
        return ''


def search():

    """
    ### Search By Smiles
    """

    np_data = np.load("./data/data.npy")
    df_data = pd.read_csv("./data/data.csv")

    tab1, tab2 = st.tabs(["Molecule SMILE", 'PUBCHEM ID'])
    with tab1:
        smile = st.text_input(label='Molecule SMILE', placeholder='COC1=C(C=C(C=C1)F)C(=O)C2CCCN(C2)CC3=CC4=C(C=C3)OCCO4')
        col1, col2 = st.columns([0.6, 0.4])
        with col1:
            N = st.slider("Choose the number of closest molecules to display", 1,100,10, key=3)
        with col2:
            add_vertical_space(2)
            show_active_only = st.checkbox("Show only Active molecules", key = 10)
        if not smile:
            pass
        else:
            try:
                with st.spinner("Please wait"):
                    name = generate_name(smile)
                    st.caption(name)
                similarities = [distance(smile, df_smile) for df_smile in df_data['SMILES']]
                df_data['Chemical Distance Similarity'] = similarities
                df_data.sort_values(by='Chemical Distance Similarity', inplace=True, ascending=False)
                filtered_df = df_data.head(N)
                filtered_df.insert(0, 'Chemical Distance', filtered_df['Chemical Distance Similarity'])
                if show_active_only:
                    filtered_df = filtered_df[filtered_df['PUBCHEM_ACTIVITY_OUTCOME'] == 'Active']
                filtered_df.drop(columns='Chemical Distance Similarity', inplace=True)
                styled_filtered_df = filtered_df.style.applymap(highlight_active, subset=['PUBCHEM_ACTIVITY_OUTCOME'])
                if filtered_df.empty:
                    st.warning("No results found for the given SMILES.")
                else:
                    st.dataframe(styled_filtered_df ,
                                        column_config={
                                            "Chemical Distance": st.column_config.ProgressColumn(
                                                "Chemical Distance Similarity",
                                                help="Chemical Distance Similarity",
                                                format="%.3f",
                                                min_value=0,
                                                max_value=1,
                                            ),
                                        }, hide_index=True)
                    @st.cache_data            
                    def convert_df(df):
                        # IMPORTANT: Cache the conversion to prevent computation on every rerun
                        return df.to_csv().encode('utf-8')

                    csv = convert_df(filtered_df)

                    st.download_button(
                        label="Download results as CSV",
                        data=csv,
                        file_name='results.csv',
                        mime='text/csv',)

            except Exception as e:
                print(e)
                st.error('Invalid Smile')

    with tab2:
        pubchem_id = st.text_input(label='PUBCHEM ID', placeholder='161916')
        col1, col2 = st.columns([0.6, 0.4])
        with col1:
            N = st.slider("Choose the number of closest molecules to display", 1,100,10, key=2)
        with col2:
            add_vertical_space(2)
            show_active_only = st.checkbox("Show only Active molecules", key = 9)
        if not pubchem_id:
            pass
        else:
            try:
                smile_pub = pubchem_id_to_smiles(pubchem_id)
                with st.spinner("Please wait"):
                    name = generate_name(smile_pub)
                    st.caption(name)
                similarities = [distance(smile_pub, df_smile) for df_smile in df_data['SMILES']]
                df_data['Chemical Distance Similarity'] = similarities
                df_data.sort_values(by='Chemical Distance Similarity', inplace=True, ascending=False)
                filtered_df = df_data.head(N)
                filtered_df.insert(0, 'Chemical Distance', filtered_df['Chemical Distance Similarity'])
                if show_active_only:
                    filtered_df = filtered_df[filtered_df['PUBCHEM_ACTIVITY_OUTCOME'] == 'Active']
                filtered_df.drop(columns='Chemical Distance Similarity', inplace=True)
                styled_filtered_df = filtered_df.style.applymap(highlight_active, subset=['PUBCHEM_ACTIVITY_OUTCOME'])
                if filtered_df.empty:
                    st.warning("No results found for the given SMILES.")
                else:
                    st.dataframe(styled_filtered_df ,
                                        column_config={
                                            "Chemical Distance": st.column_config.ProgressColumn(
                                                "Chemical Distance Similarity",
                                                help="Chemical Distance Similarity",
                                                format="%.3f",
                                                min_value=0,
                                                max_value=1,
                                            ),
                                        }, hide_index=True)
                    @st.cache_data            
                    def convert_df(df):
                        # IMPORTANT: Cache the conversion to prevent computation on every rerun
                        return df.to_csv().encode('utf-8')

                    csv = convert_df(filtered_df)

                    st.download_button(
                        label="Download results as CSV",
                        data=csv,
                        file_name='results.csv',
                        mime='text/csv',)

            except Exception as e:
                print(e)
                st.error(e)