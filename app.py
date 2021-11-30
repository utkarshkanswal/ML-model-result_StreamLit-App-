import streamlit as st
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import altair as alt
from streamlit.type_util import is_sympy_expession
from error_analysis import error_anaysis
from r2_score import r2_score
from aic_bic import aic_bic_anaysis
from actual_vs_predicted import actual_vs_predicted


data_set=st.sidebar.radio('Choose Data Set ?',('OPC Sensor','PJ Sensor'))

model_type=st.sidebar.radio('Choose Model Type ?',('Machine Learning Models','Neural Network Models'))

if model_type=='Machine Learning Models':
    t = st.sidebar.radio(
    'Choose One ?', ('Error Analysis', 'R2 Score', 'Actual vs Predicted Plot'))

    if t == "Error Analysis":
        error_anaysis()
    elif t == "R2 Score":
        r2_score()
    elif t == "Actual vs Predicted Plot":
        actual_vs_predicted()
elif model_type=='Neural Network Models':
    pass        


