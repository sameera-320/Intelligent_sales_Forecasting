import streamlit as st
import pandas as pd

st.title("🧹 Data Preprocessing")

if "data" in st.session_state:

    df = st.session_state["data"]

    st.subheader("Original Dataset")
    st.dataframe(df)

    st.subheader("Missing Values")
    st.write(df.isnull().sum())

    if st.button("Clean Data"):

        rows_before = len(df)

        df = df.dropna()
        df = df.drop_duplicates()

        rows_after = len(df)

        st.session_state["data"] = df

        st.success("Data Cleaned Successfully")

        st.write(f"Rows Before Cleaning: {rows_before}")
        st.write(f"Rows After Cleaning: {rows_after}")

        st.subheader("Cleaned Dataset")
        st.dataframe(df)

else:
    st.warning("Please upload a dataset first.")