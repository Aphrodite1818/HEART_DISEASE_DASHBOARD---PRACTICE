import pandas as pd
import streamlit as st
#-----------------LOADING THE DATASET------------------#
@st.cache_data
def load_data():
    df = pd.read_csv(
        r'C:\Users\taiwo\OneDrive\Desktop\HEART DISEASE DASHBOARD\Data preprocessing and exploaration\heart_disease_dataset_with_countries_states.csv'
    )
    return df

# This is the shared dataframe everyone will import
heart_df = load_data()
