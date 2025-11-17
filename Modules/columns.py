import streamlit as st
#---------YOUR COLUMNS FUNCTIONS GO HERE---------#
#columns for every plot and  display sections can be adjusted here 



def kpi_columns(total_patients, heart_disease_rate, average_age):
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


def line_chart_column(fig_age_chol_gender):
    #---Displaying line chart in a single column---#
    with st.container(border=True):
        line_chart_col = st.columns(1, gap="large", width='stretch')
        with line_chart_col[0]:
            st.plotly_chart(fig_age_chol_gender, theme="streamlit", use_container_width=True)
    return line_chart_col



def bar_hist_chart_column(fig_age_distribution, fig_confirmed_case_count):
    #---Displaying the bar and histogram charts side by side---#
    col_1, col_2 = st.columns(2, gap="medium", border =True)  # equal width, medium gap

    with col_1:
        st.plotly_chart(fig_age_distribution, theme="streamlit", use_container_width=True)

    with col_2:
        st.plotly_chart(fig_confirmed_case_count, theme="streamlit", use_container_width=True)

    return col_1, col_2


def map_column(fig_map):
    #---Displaying the map in its own column---#
    with st.container(border=True):
        st.plotly_chart(fig_map, theme="streamlit", use_container_width=True)



if __name__ == "__main__":
    pass