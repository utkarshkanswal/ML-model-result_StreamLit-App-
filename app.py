import streamlit as st
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import altair as alt
from streamlit.type_util import is_sympy_expession
from error_analysis import error_anaysis
from r2_score import r2_score
from aic_bic import aic_bic_anaysis
from Deep_Learning.error_analysis_dl import error_anaysis_dl
from Deep_Learning.accuracy import accuracy
from actual_vs_predicted import actual_vs_predicted
from error_analysispj import error_anaysispj
from Deep_Learning.actual_vs_predicted_dl import actual_vs_predicteddl
from r2_scorepj import r2_scorepj
from actual_vs_predictedpj import actual_vs_predictedpj
from Deep_Learning.accuracy_pj import accuracy_pj
from Deep_Learning.actual_vs_predicted_dl_pj import actual_vs_predicteddl_pj
from Deep_Learning.error_analysis_dl_pj import error_anaysis_dl_pj

data_set = st.sidebar.radio('Choose Data Set ?', ('OPC Sensor', 'PJ Sensor'))

model_type = st.sidebar.radio(
    'Choose Model Type ?', ('Machine Learning Models', 'Neural Network Models'))

if model_type == 'Machine Learning Models':
    t = st.sidebar.radio(
        'Choose One ?', ('Error Analysis', 'R2 Score', 'Actual vs Predicted Plot'))

    if t == "Error Analysis":
        if data_set == 'OPC Sensor':
            error_anaysis()
        elif data_set == 'PJ Sensor':
            error_anaysispj()
    elif t == "R2 Score":
        if data_set == 'OPC Sensor':
            r2_score()
        elif data_set == 'PJ Sensor':
            r2_scorepj()
    elif t == "Actual vs Predicted Plot":
        if data_set == 'OPC Sensor':
            actual_vs_predicted()
        elif data_set == 'PJ Sensor':
            actual_vs_predictedpj()

elif model_type == 'Neural Network Models':
    t = st.sidebar.radio(
        'Choose One ?', ('Error Analysis', 'Accuracy', 'Actual vs Predicted Plot'))

    if t == 'Error Analysis':
        if data_set == 'OPC Sensor':
            error_anaysis_dl()
        else:
            error_anaysis_dl_pj()

    if t == 'Accuracy':
        if data_set == 'OPC Sensor':
            accuracy()
        else:
            accuracy_pj()
    if t == 'Actual vs Predicted Plot':
        if data_set == 'OPC Sensor':
            actual_vs_predicteddl()
        else:
            actual_vs_predicteddl_pj()
