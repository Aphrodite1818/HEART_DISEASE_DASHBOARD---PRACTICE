import streamlit as st
from columns import columns
from sidebar import sidebar
from queries import query
from kpis import kpi
from plots import visualisations
from map import map_visualisation





# ------------- CONFIGURE PAGE -------------#
st.set_page_config(
    page_title='Cardio Health Analysis',
    page_icon='page icon image.jpeg',
    layout='wide',
    initial_sidebar_state='auto'
)







# ------------------PAGE TITLE -----------------------#
st.title("❤️ Global Cardio Health Analysis Dashboard")
st.markdown('##')  # line break for spacing









# ------------- SIDEBAR: GET USER SELECTIONS -------------#
country, state, age, Gender_selection, diagnosis = sidebar()









# ------------- QUERY: FILTER DATAFRAME BASED ON SELECTIONS -------------#
heart_df_filtered = query(country, state, age, Gender_selection, diagnosis)













# -------------------------DISPLAY KPIs IN COLUMNS---------------------------------------#
total_patients, heart_disease_rate, average_age = kpi(heart_df_filtered)
left_col, middle_col, right_col = columns(total_patients, heart_disease_rate, average_age)

st.markdown('---')  # horizontal line to separate sections



#------------------------------VISUALIZATIONS----------------------------------------------#
#Plots visualizations
fig_age_distribution , fig_age_chol_gender , fig_confirmed_case_count  = visualisations(heart_df_filtered)



#Map visualization
fig_map = map_visualisation(heart_df_filtered)