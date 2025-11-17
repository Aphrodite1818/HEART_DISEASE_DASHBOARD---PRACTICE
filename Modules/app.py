import streamlit as st
from columns import kpi_columns , line_chart_column , bar_hist_chart_column , map_column
from sidebar import sidebar
from queries import query
from kpis import kpi
from plots import visualisations
from map import map_visualisation


# ------------- CONFIGURE PAGE -------------#
st.set_page_config(
    page_title='Cardio Health Analysis',
    page_icon=r'C:\Users\taiwo\OneDrive\Desktop\HEART DISEASE DASHBOARD\images and icons\page icon image.jpeg',
    layout='wide',
    initial_sidebar_state='auto'
    )




def app():
 # ------------------PAGE TITLE -----------------------#
    st.title("❤️ Global Cardio Health Analysis Dashboard")
    st.markdown('##')  # line break for spacing









    # ------------- SIDEBAR: GET USER SELECTIONS -------------#
    country, state, age, Gender_selection, diagnosis = sidebar()

    st.logo(
    image = r"C:\Users\taiwo\OneDrive\Desktop\HEART DISEASE DASHBOARD\images and icons\sidebar icon image.png",  # Path to the logo image
        icon_image=r"C:\Users\taiwo\OneDrive\Desktop\HEART DISEASE DASHBOARD\images and icons\sidebar icon image.png"  # Optional: icon for when sidebar is closed
    )







    # ------------- QUERY: FILTER DATAFRAME BASED ON SELECTIONS -------------#
    heart_df_filtered = query(country, state, age, Gender_selection, diagnosis)













    # -------------------------DISPLAY KPIs IN COLUMNS---------------------------------------#
    total_patients, heart_disease_rate, average_age = kpi(heart_df_filtered)
    left_col, middle_col, right_col = kpi_columns(total_patients, heart_disease_rate, average_age)

    st.markdown('---')  # horizontal line to separate sections



    #------------------------------VISUALIZATIONS----------------------------------------------#
    #tTHIS FUNCTIONS RETURNS ALL THE THREE CHARTS ABOUT THE DATASET
    fig_age_distribution, fig_age_chol_gender, fig_confirmed_case_count = visualisations(heart_df_filtered)


    # Display the line chart in a single column
    line_chart_col = line_chart_column(fig_age_chol_gender)



    # Display the bar and histogram charts side by side
    bar_hist_col_1, bar_hist_col_2 = bar_hist_chart_column(fig_age_distribution, fig_confirmed_case_count)


    #Map visualization
    fig_map = map_visualisation(heart_df_filtered)

    # Display the map in its own section
    map_col = map_column(fig_map)


if __name__ == "__main__":
    app()