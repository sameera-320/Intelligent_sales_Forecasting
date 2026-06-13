import streamlit as st
import pandas as pd

st.title("📂 Data Upload")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.session_state["data"] = df

    st.success("Dataset Uploaded Successfully")

    st.dataframe(df.head())

if st.button("Load Sample Dataset"):
    st.info("Sample Dataset Loaded")