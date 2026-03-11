import streamlit as st
import pandas as pd
from engine import QueryEngine

st.title("QueryFlow PoC")
st.sidebar.title("Power Query Steps")

# Sample Data
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame({
        'Product': ['Laptop', 'Mouse', 'Keyboard', 'Laptop', 'Mouse'],
        'Sales': [1000, 20, 50, 1200, 25]
    })
    st.session_state.data2 = pd.DataFrame({
        'Product': ['Laptop', 'Mouse'],
        'Category': ['Electronics', 'Peripherals']
    })

engine = QueryEngine(st.session_state.data, st.session_state.data2)

# UI for Transformation Steps
step_type = st.sidebar.selectbox("Add Step", ["Filter", "Group By", "Append", "Merge"])

if step_type == "Filter":
    col = st.sidebar.selectbox("Column", st.session_state.data.columns)
    val = st.sidebar.text_input("Value")
    if st.sidebar.button("Apply Filter"):
        engine.add_step('filter', {'column': col, 'operator': '=', 'value': f"'{val}'"})
elif step_type == "Append":
    if st.sidebar.button("Append df2"):
        engine.add_step('append', {})
elif step_type == "Merge":
    left_col = st.sidebar.text_input("Left Key")
    right_col = st.sidebar.text_input("Right Key")
    if st.sidebar.button("Merge"):
        engine.add_step('merge', {'left_col': left_col, 'right_col': right_col})

# Display Result
st.write("Current Data:")
st.dataframe(st.session_state.data)

st.write("Generated SQL:")
st.code(engine.get_query())
