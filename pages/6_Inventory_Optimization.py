import streamlit as st

st.title("📦 Inventory Optimization")

stock = st.number_input("Current Stock", value=100)

if st.button("Optimize Inventory"):
    recommended = stock + 20

    st.metric(
        "Recommended Inventory",
        recommended
    )