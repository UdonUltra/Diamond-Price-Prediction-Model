import streamlit as st
import pandas as pd
# import joblib as jb
import eda
import prediction


#header
"""
# Milestone 2
**Name    : Frederick Kurniawan Putra**

**Batch   : HCK016**

This is model deployment of Diamond Price Prediction.
"""



PAGES = {
    "Eda": eda,
    "Prediction": prediction
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()