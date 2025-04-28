import streamlit as st
import plotly.express as px

st.title("🛬 Route CO₂ Insights")

if "df" in st.session_state and st.session_state["df"] is not None:
    df = st.session_state["df"]
    route_co2 = df.groupby(['Origin', 'Destination'])['Adjusted_CO2_kg'].sum().reset_index()
    fig = px.bar(route_co2, x='Origin', y='Adjusted_CO2_kg', color='Destination', title="Top CO₂ Emitting Routes")
    st.plotly_chart(fig)
else:
    st.warning("No data available! Switch to Historic Data mode.")