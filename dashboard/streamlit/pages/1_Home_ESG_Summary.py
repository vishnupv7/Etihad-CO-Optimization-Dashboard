import streamlit as st

st.title("🌍 ESG Validation Summary")

if "df" in st.session_state and st.session_state["df"] is not None:
    df = st.session_state["df"]
    st.metric("Total Flights", f"{len(df):,}")
    st.metric("Total Fuel Burn (kg)", f"{df['Adjusted_Fuel_Burn_kg'].sum():,.2f}")
    st.metric("Total CO₂ Emissions (kg)", f"{df['Adjusted_CO2_kg'].sum():,.2f}")
    st.metric("Total Estimated Revenue (USD)", f"${df['Estimated_Revenue_USD'].sum():,.2f}")
else:
    st.warning("No data available! Switch to Historic Data mode.")