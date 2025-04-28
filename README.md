# ✈️ Etihad Airways - CO₂ Optimization Dashboard

An end-to-end Machine Learning and Data Engineering project focused on optimizing fuel efficiency and CO₂ emissions for Etihad Airways operations.

---

## 📈 Project Pipeline
- Data Collection (OpenSky API, OpenWeatherMap API, ICAO Emissions Database, Etihad ESG Reports)
- Data Cleaning & Schema Integration
- CO₂ Emissions Modeling (Distance, Aircraft Type, Fuel Burn)
- Weather Impact Adjustment (Wind, Pressure)
- Route Deviation Detection (Holding Patterns, Altitude Drift, Unplanned Reroutes)
- ML Anomaly Detection (RandomForest Model)
- ESG Validation (Comparison against 2022 Report)
- Streamlit Dashboard Deployment

---

## 🛠 Folder Structure

Etihad_CO2_Optimization_Dashboard/
├── data/
│   ├── raw/
│   ├── processed/
├── dashboard/
│   ├── streamlit/
├── notebooks/
├── docs/
├── README.md
├── requirements.txt

---

## 📊 Dashboard Features
- ESG Validation Metrics (Flights, Fuel Burn, CO₂ Emissions, ESG Match %)
- Route CO₂ Analysis (Top Emitting Routes)
- Aircraft Type CO₂ Insights
- Weather Penalty Visualization
- ML-based Anomaly Detection (Fuel & CO₂ Outliers)

---

## 🚀 How to Launch Locally

streamlit run dashboard/streamlit/app.py

---

## 🌍 Live Demo (Streamlit Cloud)

➡️ Coming Soon After Deployment!

---

## 📚 Data Sources
- OpenSky Network
- OpenWeatherMap API
- ICAO Emissions Database
- Etihad Airways ESG Report 2022

---

## 🛡️ License
This project is for educational and demonstration purposes only. It is not officially affiliated with Etihad Airways.