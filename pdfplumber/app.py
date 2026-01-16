import streamlit as st
import pdfplumber
import pandas as pd

st.title("PDF → Excel")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")
if uploaded_file:
    with pdfplumber.open(uploaded_file) as pdf:
        st.write(f"Pages: {len(pdf.pages)}")
