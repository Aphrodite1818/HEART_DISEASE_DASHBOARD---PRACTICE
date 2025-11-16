import streamlit as st




def columns(total_patients, heart_disease_rate, average_age):
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

    return left_col, middle_col, right_col


