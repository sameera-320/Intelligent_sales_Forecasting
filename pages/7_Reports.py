import streamlit as st

st.title("📄 Reports")

report = """
Sales Forecast Report

Generated Successfully
"""

st.download_button(
    label="Download Report",
    data=report,
    file_name="forecast_report.txt",
    mime="text/plain"
)