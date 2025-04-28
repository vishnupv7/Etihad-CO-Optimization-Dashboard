import streamlit as st
import plotly.express as px

st.title("💵 Revenue Insights")

if "df" in st.session_state and st.session_state["df"] is not None:
    df = st.session_state["df"]
    rev_routes = df.groupby(['Origin', 'Destination'])['Estimated_Revenue_USD'].sum().reset_index()
    fig = px.bar(rev_routes, x='Origin', y='Estimated_Revenue_USD', color='Destination', title="Top Revenue Generating Routes")
    st.plotly_chart(fig)
else:
    st.warning("No data available! Switch to Historic Data mode.")