import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 EDA Analysis")

if "data" in st.session_state:

    df = st.session_state["data"]

    st.subheader("Dataset Preview")
    st.dataframe(df)

    # Sales by Product
    if "Product" in df.columns and "Sales" in df.columns:

        sales_product = df.groupby("Product")["Sales"].sum().reset_index()

        fig1 = px.bar(
            sales_product,
            x="Product",
            y="Sales",
            title="Sales by Product"
        )
        st.plotly_chart(fig1, use_container_width=True)

    # Sales by Region
    if "Region" in df.columns and "Sales" in df.columns:

        sales_region = df.groupby("Region")["Sales"].sum().reset_index()

        fig2 = px.pie(
            sales_region,
            names="Region",
            values="Sales",
            title="Sales Distribution by Region"
        )
        st.plotly_chart(fig2, use_container_width=True)

    # Inventory
    if "Inventory" in df.columns:

        fig3 = px.histogram(
            df,
            x="Inventory",
            title="Inventory Distribution"
        )
        st.plotly_chart(fig3, use_container_width=True)

    # Profit
    if "Profit" in df.columns:

        fig4 = px.box(
            df,
            y="Profit",
            title="Profit Analysis"
        )
        st.plotly_chart(fig4, use_container_width=True)

else:
    st.warning("Upload dataset first")