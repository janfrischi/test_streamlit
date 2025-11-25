import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="My First Streamlit App", page_icon="🚀")

st.title("Hello, Streamlit! 👋")
st.write(
    """
    This is a **basic Streamlit app**.

    Use the sidebar to change the configuration and see how the app updates.
    """
)

# Sidebar controls
st.sidebar.header("Controls")
num_points = st.sidebar.slider("Number of random data points", min_value=10, max_value=500, value=100)
show_table = st.sidebar.checkbox("Show raw data table", value=True)

# Generate some random data
data = pd.DataFrame(
    np.random.randn(num_points, 2),
    columns=["x", "y"]
)

st.subheader("Random data scatter plot")
st.scatter_chart(data)

if show_table:
    st.subheader("Raw data")
    st.dataframe(data)
