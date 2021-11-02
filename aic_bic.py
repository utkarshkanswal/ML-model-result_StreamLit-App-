import streamlit as st
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import altair as alt

xgboost_list = [0.00002285973898022485,
                0.001955862053424563, 0.00478118593867932]
randomforest_list = [0.00005511369987097619,
                     0.0040103400631165955, 0.007423860173183233]
var_list = [0.00012164231497931546, 0.007302538086412745,
            0.011029157491817562, -3623002.3803782254, -3621909.3004321116]
vma_list = [0.00012161140493576916, 0.007300713574989763,
            0.011027756115174526, -3623029.066632705, -3621935.986686591]
varmax_list = [0.00012164231712440681, 0.007302540667162326,
               0.011029157589063945, -3622904.383916931, -3621361.2122283005]


def aic_bic_anaysis():
    st.sidebar.subheader("Choose Model ?")
    select_model3 = st.sidebar.checkbox('Vector Auto Regression')
    select_model4 = st.sidebar.checkbox('Vector Moving Average')
    select_model5 = st.sidebar.checkbox(
        'Vector Auto Regression Moving Average')

    models = list()

    if select_model3:
        models.append("VAR")

    if select_model4:
        models.append("VMA")

    if select_model5:
        models.append("VARMA")

    st.sidebar.subheader("Choose Value ?")

    select_error1 = st.sidebar.checkbox('AIC')
    select_error2 = st.sidebar.checkbox('BIC')

    errors = list()

    if select_error1:
        errors.append("AIC")

    if select_error2:
        errors.append("BIC")

    arr = list()
    j = 0
    for m in models:
        l = list()
        for e in errors:
            if e == "AIC" and m == "VAR":
                l.append(var_list[3])
            if e == "BIC" and m == "VAR":
                l.append(var_list[4])
            if e == "AIC" and m == "VMA":
                l.append(vma_list[3])
            if e == "BIC" and m == "VMA":
                l.append(vma_list[4])
            if e == "AIC" and m == "VARMA":
                l.append(varmax_list[3])
            if e == "BIC" and m == "VARMA":
                l.append(varmax_list[4])

        arr.append(l)

    temp = np.array(arr).transpose()

    if len(models) > 0 and len(errors) > 0:
        st.header("Plot for AIC and BIC for different Models")
        chart_data = pd.DataFrame(temp, errors, columns=models)
        st.table(chart_data)
        st.line_chart(chart_data, height=450)
    else:
        title = st.title("Welcome to Air Quality Result Analysis Web App")

        st.markdown("Comparative analysis on dataset of different machine learning models  and find out the best model having more accurate predictions of air quality .")
        st.markdown("The dataset is a collection of sensor data for 7 different locations of Malaysia which is collected through OPC sensors. These data are for 15 months that are from March 2019 to May 2020. These data are in CSV or Excel files. These data are saved in month wise format. These data have 57 columns and 35847 rows. These data are recorded for every hour.")
        st.markdown("For the sensor data, out of these 57 features(i.e. number of columns) we are taking 5 features as our input target and 7 as our output target. The input targets are Node value, date, time, external temperature and external RH. The output targets are NO2 ppb, O3 ppb, NO ppb, CO ppb, PM1, PM2.5 and PM10.We are processing the data before sending it to the network. ")
