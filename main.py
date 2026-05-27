import streamlit as st
#from analyse import HF_Zonen

tab1, tab2 = st.tabs(["EKG-Data", "Power-Data"])

with tab1:
    st.header("EKG-Data")
    st.write("# My Plot")

with tab2:
    st.header("Power-Data")
