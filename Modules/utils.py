import pandas as pd
import streamlit as st


#-------THE UTILS MODULE WILL CONTAIN ALL THE SHARED RESOURCES LIKE DATAFRAMES, FUNCTIONS ETC.-------#

#you can change the dataset here if needed
#NB: MAKE SURE THE DATA SET MATCHES THE SAME STRUCTURE THE DASHBOARD WAS BUILT WITH
#YOU CAN CHECK PREPROESSING.IPYNB TO SEE THE DATA CLEANING STEPS APPLIED TO THE DATASET USED TO BUILD THE DASHBOARD


#-----------------LOADING THE DATASET------------------#
@st.cache_data
def load_data():
    df = pd.read_csv(
        r'C:\Users\taiwo\OneDrive\Desktop\HEART DISEASE DASHBOARD\Data preprocessing and exploaration\heart_disease_dataset_with_countries_states.csv'
    )
    return df

# This is the shared dataframe everyone will import
heart_df = load_data()


if __name__ == "__main__":
    print(heart_df.head())