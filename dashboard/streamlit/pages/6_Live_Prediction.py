import streamlit as st

st.title("📡 Live Flight Prediction (Coming Soon!)")

if st.session_state["data_mode"] == "Live":
    st.success("Live Mode Selected! Live flight predictions will be enabled here soon 🚀.")
else:
    st.warning("Switch to Live Data mode to use this page.")