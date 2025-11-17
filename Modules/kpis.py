import streamlit as st
#---------YOUR KPI FUNCTIONS GO HERE---------#
#You can define all your kpi related functions here


def kpi(heart_df_filtered):
    total_patients = heart_df_filtered.shape[0]
    heart_disease_rate = f"📉{((heart_df_filtered['target'] == 1).sum() / len(heart_df_filtered) * 100):.2f}"
    average_age = round(heart_df_filtered['age'].mean())

    return total_patients, heart_disease_rate, average_age

if __name__ == "__main__":
    print("This is the kpis module.")