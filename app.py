import streamlit as st
import pandas as pd
from engine import QueryEngine

st.title("QueryFlow PoC")
st.sidebar.title("Power Query Steps")

# 1. ADDED: File Uploader
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    st.session_state.data = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully!")

# 2. Default to Sample Data if no file is uploaded
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame({
        'Product': ['Laptop', 'Mouse', 'Keyboard', 'Laptop', 'Mouse'],
        'Sales': [1000, 20, 50, 1200, 25]
    })

# Initialize Engine
engine = QueryEngine(st.session_state.data)

# UI for Transformation Steps
step_type = st.sidebar.selectbox("Add Step", ["Filter", "Group By", "Append", "Merge"])

# ... (Keep the rest of your Filter/Group By logic here)

# Display Result
st.write("Current Data:")
st.dataframe(st.session_state.data)

st.write("Generated SQL:")
st.code(engine.get_query())
