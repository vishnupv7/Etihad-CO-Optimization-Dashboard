import streamlit as st
import plotly.express as px

st.title("⚡ ML Anomaly Detection")

if "df" in st.session_state and st.session_state["df"] is not None:
    df = st.session_state["df"]
    top_anomalies = df.sort_values(by='Anomaly_Score', ascending=False).head(50)
    fig = px.bar(top_anomalies, x='Callsign', y='Anomaly_Score', color='Anomaly_Score', title="Top 50 High Anomaly Flights")
    st.plotly_chart(fig)
else:
    st.warning("No data available! Switch to Historic Data mode.")