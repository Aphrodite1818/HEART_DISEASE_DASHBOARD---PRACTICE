import plotly.express as px
import streamlit as st





def visualisations(heart_df_filtered):
#--------------------------------------------VISUALISATIONS----------------------------------------------------#
    #1. AGE DISTRIBUTION BAR CHART
    age_distribution =(heart_df_filtered['age'])

    fig_age_distribution = px.histogram(
        heart_df_filtered,        # filtered DataFrame
        x='age',                  # column name as string
        nbins=20,                 # number of bins
        template='plotly_white',
        title='<b>Age Distribution of Patients</b>',
        color = 'Gender'
    )

    fig_age_distribution.update_layout(
        xaxis_title='Age',
        yaxis_title='Number of Patients'
    )

    st.plotly_chart(fig_age_distribution, theme="streamlit", use_container_width=True)





    #2 Heart_disease_rate compared with age group vs cholestrol line chart
    age_chol_gender = heart_df_filtered.groupby(['age', 'Gender'])['chol'].mean().reset_index()

    fig_age_chol_gender = px.line(
        age_chol_gender,
        x='age',
        y='chol',
        color='Gender',
        title='Average Cholesterol by Age and Gender',
        markers=True
    )

    st.plotly_chart(fig_age_chol_gender, use_container_width=True)






    #3 Heart_disease positive count bar chart in each country

    positive_cases = heart_df_filtered[heart_df_filtered['target'] == 1]

    # Count positive cases per country
    confirmed_country_count = (
        positive_cases.groupby('Country')
        .size()
        .reset_index(name='positive_count')
    )

    # Plot a bar chart
    fig_confirmed_case_count = px.bar(confirmed_country_count, 
                x='Country', 
                y='positive_count', 
                title='Positive Heart Disease Cases by Country',
                labels={'positive_count':'Number of Positive Cases'},
                color='positive_count',
                color_continuous_scale='blues')

    st.plotly_chart(fig_confirmed_case_count, use_container_width=True)


    return fig_age_distribution , fig_age_chol_gender , fig_confirmed_case_count