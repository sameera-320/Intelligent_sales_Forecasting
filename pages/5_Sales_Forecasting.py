import streamlit as st
import pandas as pd

st.title("📈 Sales Forecasting")

if "data" in st.session_state:
    df = st.session_state["data"]

    st.line_chart(df.select_dtypes(include="number"))

    if st.button("Generate Forecast"):
        st.success("Forecast Generated")
else:
    st.warning("Upload data first.")