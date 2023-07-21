
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
from sklearn.neural_network import MLPClassifier

def predict_with_model(smile, model_path):
    molecule = Chem.MolFromSmiles(smile)
    x = np.array(AllChem.RDKFingerprint(molecule, fpSize=2048))
    # Load the pickled model
    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    # Make the prediction using the loaded model
    y = model.predict([x])
    return y 

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


def predict():

    """
    ### Search By Smiles
    """


    data = np.load("./data/data.npy")



    tab1, tab2= st.tabs(["Molecule SMILE",'PUBCHEM ID'])
    with tab1:
            smile = st.text_input(label = 'Molecule SMILE', placeholder = 'COC1=C(C=C(C=C1)F)C(=O)C2CCCN(C2)CC3=CC4=C(C=C3)OCCO4')
            if not smile:
                pass 
            else:
                try:
                    name = generate_name(smile)
                    st.caption(name)
                    render = makeblock(smile)
                    render_mol(render)
                    progress_text = "Operation in progress. Please wait."
                    with st.spinner(progress_text):
                        mol_weight = cd.MolWt(Chem.MolFromSmiles(smile))
                        similiarity = calculate_distance(smile, data)
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Molecular Weight", round(mol_weight, 2), f"{round((mol_weight - 352),2)}")
                    col2.metric("Similiraity", f"{round(similiarity,2)}%" , f"{round((similiarity - 0.11),2)}%", delta_color = "inverse")
                    if passes_lipinski_rule(smile):
                        col3.metric("Lipinski", "Pass")
                    elif passes_lipinski_rule(smile) == False:
                        col3.metric("Lipinski", "Fail")
                    if predict_with_model(smile, "./model.pkl") == 1:
                        st.success('Active', icon="✅")
                    elif predict_with_model(smile, "./model.pkl") == 0:
                        st.error('Inactive', icon="❌")
                except Exception as e:
                    print(e)
                    st.error('Invalid Smile')




    with tab2:
        pub = st.text_input(label = 'PUBCHEM ID', placeholder = '161916')
        if not pub:
            pass 
        else:
            try:
                smile = pubchem_id_to_smiles(pub)
                name = generate_name(smile)
                st.caption(name)
                render = makeblock(smile)
                render_mol(render)
                progress_text = "Operation in progress. Please wait."
                with st.spinner(progress_text):
                    mol_weight = cd.MolWt(Chem.MolFromSmiles(smile))
                    similiarity = calculate_distance(smile, data)
                col1, col2, col3 = st.columns(3)
                col1.metric("Molecular Weight", round(mol_weight, 2), f"{round((mol_weight - 352),2)}")
                col2.metric("Similiraity", f"{round(similiarity,2)}%" , f"{round((similiarity - 0.11),2)}%", delta_color = "inverse")
                if passes_lipinski_rule(smile):
                    col3.metric("Lipinski", "Pass")
                elif passes_lipinski_rule(smile) == False:
                    col3.metric("Lipinski", "Fail")
                st.success('Active', icon="✅")

            except Exception as e:
                print(e)
                st.error('Invalid PubchemID')