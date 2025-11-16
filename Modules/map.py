import plotly.express as px
import streamlit as st

#Adding map

@st.cache_data
def map_visualisation(heart_df_filtered):
    fig_map = px.scatter_mapbox(
        heart_df_filtered,
        lat='C_lat',
        lon='C_lon',
        hover_name='Country',             # shows state on hover
        hover_data=['Country','Diagnosis'],  # extra info
        color='Diagnosis',              # color points by diagnosis
        color_discrete_map={1: 'red', 0: 'green'},  # positive = red, negative = green
        zoom=1,
        height=600,
        opacity=0.7                    # make points slightly transparent
    )

    fig_map.update_layout(
        mapbox_style='open-street-map',
        paper_bgcolor='rgba(0,0,0,0)',   # transparent background
        plot_bgcolor='rgba(0,0,0,0)',
        margin={"r":0,"t":0,"l":0,"b":0}
    )

    st.plotly_chart(fig_map, use_container_width=True)

    return fig_map