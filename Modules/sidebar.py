# sidebar.py
import streamlit as st
from utils import heart_df

def sidebar():
    st.sidebar.header("CLICK HERE TO FILTER DATASET")

    country = st.sidebar.multiselect(
        "Select the country",
        options=heart_df['Country'].unique(),
        default=heart_df['Country'].unique(),
        key="country"
    )

    age = st.sidebar.slider(
        "Select age range",
        min_value=int(heart_df['age'].min()),
        max_value=int(heart_df['age'].max()),
        value=(int(heart_df['age'].min()), int(heart_df['age'].max())),
        key="age"
    )

    Gender_selection = st.sidebar.multiselect(
        "Select gender",
        options=heart_df['Gender'].unique(),
        default=heart_df['Gender'].unique(),
        key="gender"
    )

    selected_country_states = heart_df.loc[heart_df['Country'].isin(country), 'State'].unique()
    state = st.sidebar.multiselect(
        "Select state",
        options=selected_country_states,
        default=selected_country_states,
        key="state"
    )

    diagnosis = st.sidebar.multiselect(
        "Select diagnosis",
        options=heart_df['Diagnosis'].unique(),
        default=heart_df['Diagnosis'].unique(),
        key="diagnosis"
    )

    return country, state, age, Gender_selection, diagnosis
