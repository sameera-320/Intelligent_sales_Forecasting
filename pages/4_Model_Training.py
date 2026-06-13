import streamlit as st
import time

st.title("🤖 Model Training")

if st.button("Train Model"):

    progress = st.progress(0)

    for i in range(100):
        time.sleep(0.02)
        progress.progress(i + 1)

    st.success("Model Trained Successfully")