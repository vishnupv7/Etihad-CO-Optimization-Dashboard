import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Etihad CO₂ Optimization Dashboard", page_icon="✈️", layout="wide")

st.sidebar.title("Dashboard Settings")
mode = st.sidebar.radio("Select Data Mode:", ["Historic Data", "Live Data"])

@st.cache_data
def load_historic_data():
    return pd.read_csv('data/processed/etihad_dashboard_demo_ml.csv')

if mode == "Historic Data":
    df = load_historic_data()
    st.session_state["data_mode"] = "Historic"
    st.session_state["df"] = df
else:
    st.session_state["data_mode"] = "Live"
    st.session_state["df"] = None

st.title("✈️ Etihad Airways - CO₂ Optimization Dashboard")
st.markdown("Navigate using the sidebar to access different modules 🚀.")