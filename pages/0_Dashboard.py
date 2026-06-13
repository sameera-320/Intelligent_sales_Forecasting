import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Intelligent Sales Forecasting Dashboard")

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Sales", "₹1,25,000", "+12%")

with col2:
    st.metric("Orders", "90", "+5")

with col3:
    st.metric("Products", "5")

with col4:
    st.metric("Forecast Accuracy", "94%")

st.divider()

# Navigation Buttons
st.subheader("🚀 Quick Navigation")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📂 Data Upload", use_container_width=True):
        st.switch_page("pages/1_Data_Upload.py")

with col2:
    if st.button("🧹 Data Preprocessing", use_container_width=True):
        st.switch_page("pages/2_Data_Preprocessing.py")

with col3:
    if st.button("📊 EDA Analysis", use_container_width=True):
        st.switch_page("pages/3_EDA_Analysis.py")

col4, col5, col6 = st.columns(3)

with col4:
    if st.button("🤖 Model Training", use_container_width=True):
        st.switch_page("pages/4_Model_Training.py")

with col5:
    if st.button("📈 Sales Forecasting", use_container_width=True):
        st.switch_page("pages/5_Sales_Forecasting.py")

with col6:
    if st.button("📦 Inventory Optimization", use_container_width=True):
        st.switch_page("pages/6_Inventory_Optimization.py")

st.divider()

if st.button("📄 Reports", use_container_width=True):
    st.switch_page("pages/7_Reports.py")

st.divider()

# Dataset Visualization
if "data" in st.session_state:

    df = st.session_state["data"]

    st.subheader("📋 Dataset Preview")
    st.dataframe(df.head())

    # Sales Trend Graph
    if "Date" in df.columns and "Sales" in df.columns:

        fig = px.line(
            df,
            x="Date",
            y="Sales",
            title="📈 Sales Trend"
        )

        st.plotly_chart(fig, use_container_width=True)

else:
    st.info("📂 Upload a dataset to view charts and analytics.")

st.divider()

st.subheader("📌 Project Workflow")

st.write("""
1️⃣ Upload Dataset

2️⃣ Preprocess Data

3️⃣ Perform EDA Analysis

4️⃣ Train Model

5️⃣ Forecast Sales

6️⃣ Optimize Inventory

7️⃣ Generate Reports
""")

st.success("Use the buttons above or the sidebar to navigate.")