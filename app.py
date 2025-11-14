import pandas as pd
import streamlit as st
import plotly.express as px


#-------------CONFIGURING THE PAGE----------------#
st.set_page_config(page_title = 'Cardio Health Analysis',
                   page_icon='page icon image.jpeg',layout='wide',initial_sidebar_state='auto')



#-------------LOADING THE DATA---------------------#
@st.cache_data
def load_data():
    loaded_data = pd.read_csv(r'C:\Users\taiwo\OneDrive\Desktop\HEART DISEASE DASHBOARD\Data preprocessing and exploaration\heart_disease_dataset_with_countries_states.csv')
    return loaded_data

heart_df = load_data()

#st.dataframe(heart_df)


#-----------------CREATING SIDEBAR FOR FILTERUNG------------------#
st.sidebar.header("CLICK HERE TO FILTER DATASET")


#--------------SIDEBAR FILTER 1 ----------------#
country = st.sidebar.multiselect(
    "select the country here",
    options = heart_df['Country'].unique(),
    default = heart_df['Country'].unique()
    )



#--------------SIDEBAR FILTER 2----------------#
age = st.sidebar.slider(
    "Select the age range",
    min_value = int(heart_df['age'].min()),
    max_value = int(heart_df['age'].max()),
    value = (int(heart_df['age'].min()), int(heart_df['age'].max())),
)

#--------------SIDEBAR FILTER 3----------------#
Gender_selection = st.sidebar.multiselect(
    "select the gender here",
    options=heart_df['Gender'].unique(),
    default = heart_df['Gender'].unique()
)


#----------------SIDEBAR FILTER 4----------------#

selected_country_states = heart_df.loc[heart_df['Country'].isin(country)]['State'].unique()
state = st.sidebar.multiselect(
    "select the state here",
    options = selected_country_states,
    default = selected_country_states
)

#---------SIDEBAR FILTER 5----------------#
diagnosis = st.sidebar.multiselect(
    "select the diagnosis here",
    options = heart_df['Diagnosis'].unique(),
    default = heart_df['Diagnosis'].unique()
)



#-----------------USING QUERY FUNCTION TO FILTER DATASET BASED ON SIDEBAR SELECTIONS------------------#
# Start with the full dataframe
heart_df_filtered = heart_df.copy()

# Country filter
if country:  # only apply if user selected at least one country
    heart_df_filtered = heart_df_filtered.query("Country in @country")

# State filter
if state:
    heart_df_filtered = heart_df_filtered.query("State in @state")

# Gender filter
if Gender_selection:
    heart_df_filtered = heart_df_filtered.query("Gender in @Gender_selection")

# Age range filter (always applied because slider always returns a range)
heart_df_filtered = heart_df_filtered.query("age >= @age[0] & age <= @age[1]")

# Diagnosis filter
if diagnosis:
    heart_df_filtered = heart_df_filtered.query("Diagnosis in @diagnosis")




#-----------------MAINPAGE FOR THE DASHBOARD------------------#
#calculating KPI'S
st.title("❤️ Global Cardio Health Analysis Dashboard")
st.markdown('##') #this just creates a new line break for better spacing


total_patients = heart_df_filtered.shape[0]
heart_disease_rate = f"📉{((heart_df_filtered['target'] == 1).sum() / len(heart_df_filtered) * 100):.2f}"
average_age = round(heart_df_filtered['age'].mean())


#----------------DISPLAYING THE KPI'S USING COLUMNS------------------#
left_col, middle_col, right_col = st.columns(3, border=True, gap="large", width='stretch')
with left_col:
    st.subheader('Total Patients Globally')
    st.subheader(f"{total_patients:,}")

with middle_col:
    st.subheader('Global Heart Disease Rate')
    st.subheader(f"{heart_disease_rate}%")

with right_col:
    st.subheader('Average Age Globally')
    st.subheader(f"{average_age} years")



st.markdown('---')  #this creates a horizontal line to separate sections



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


#2 Heart_disease_rate compared with age group line chart
