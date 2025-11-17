import pandas as pd
import streamlit as st
import os

#-------THE UTILS MODULE WILL CONTAIN ALL THE SHARED RESOURCES LIKE DATAFRAMES, FUNCTIONS ETC.-------#

#-----------------LOADING THE DATASET------------------#
@st.cache_data
def load_data():
    # Streamlit runs from repo root, so we can use a relative path from there
    csv_path = os.path.join("Data preprocessing and exploration", "heart_disease_dataset_with_countries_states.csv")
    
    # Optional: check if the file exists
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV file not found at {os.path.abspath(csv_path)}")
    
    # Load CSV
    df = pd.read_csv(csv_path)
    return df

# Shared dataframe
heart_df = load_data()

# Optional test run
if __name__ == "__main__":
    print(heart_df.head())
