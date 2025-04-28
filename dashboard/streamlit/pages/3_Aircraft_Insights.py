import streamlit as st
import plotly.express as px

st.title("✈️ Aircraft CO₂ Insights")

if "df" in st.session_state and st.session_state["df"] is not None:
    df = st.session_state["df"]
    acft_co2 = df.groupby('Aircraft_Code')['Adjusted_CO2_kg'].sum().reset_index()
    fig = px.pie(acft_co2, names='Aircraft_Code', values='Adjusted_CO2_kg', title='CO₂ Emission Share by Aircraft')
    st.plotly_chart(fig)
else:
    st.warning("No data available! Switch to Historic Data mode.")