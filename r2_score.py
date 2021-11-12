from logging import error
import streamlit as st
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import altair as alt

data_type = ['Test Data', 'Train Data']

xgboost_list = [0.8623226304872951, 0.9426134014720243]
randomforest_list = [0.7157456297425531, 0.7204765644279367]
var_list = [0.3600870655999349, 0.33375415804112096]
vma_list = [0.36034097852264296, 0.3339029193613109]
varmax_list = [0.36008704455714285, 0.33375415451011453]
knn_list = [0.8029100802530473, 0.8710465258994434]
svm_list = [-47.4020930609896, -36.36515905532197]
lstm = [0.9267, 0.9241]


def r2_score():
    st.sidebar.subheader("Choose Model ?")
    select_model1 = st.sidebar.checkbox('Xgboost')
    select_model2 = st.sidebar.checkbox('Random Forest')
    select_model3 = st.sidebar.checkbox('Vector Auto Regression')
    select_model4 = st.sidebar.checkbox('Vector Moving Average')
    select_model5 = st.sidebar.checkbox(
        'Vector Auto Regression Moving Average')
    select_model6 = st.sidebar.checkbox('K Nearest Neighbour')
    select_model7 = st.sidebar.checkbox('Support Vector Machine')
    select_model8 = st.sidebar.checkbox('LSTM')

    models = list()
    arr = list()

    if select_model1:
        arr.append(xgboost_list)
        models.append("Xgboost")

    if select_model2:
        arr.append(randomforest_list)
        models.append("Random Forest")

    if select_model3:
        arr.append(var_list)
        models.append("VAR")

    if select_model4:
        arr.append(vma_list)
        models.append("VMA")

    if select_model5:
        arr.append(varmax_list)
        models.append("VARMA")

    if select_model6:
        arr.append(knn_list)
        models.append("KNN")

    if select_model7:
        arr.append(svm_list)
        models.append("SVM")

    if select_model8:
        arr.append(lstm)
        models.append("LSTM")

    errors = ['R2 Score on Test', 'R2 Score on Train']
    if len(models) > 0:
        st.header("Plot for R2 Score different Models")
        chart_data = pd.DataFrame(np.array(arr), models, columns=errors)
        st.table(chart_data)
        st.bar_chart(chart_data, height=450)
    else:
        title = st.title("Welcome to Air Quality Result Analysis Web App")
        st.markdown("Comparative analysis on dataset of different machine learning models  and find out the best model having more accurate predictions of air quality .")
        st.markdown("The dataset is a collection of sensor data for 7 different locations of Malaysia which is collected through OPC sensors. These data are for 15 months that are from March 2019 to May 2020. These data are in CSV or Excel files. These data are saved in month wise format. These data have 57 columns and 35847 rows. These data are recorded for every hour.")
        st.markdown("For the sensor data, out of these 57 features(i.e. number of columns) we are taking 5 features as our input target and 7 as our output target. The input targets are Node value, date, time, external temperature and external RH. The output targets are NO2 ppb, O3 ppb, NO ppb, CO ppb, PM1, PM2.5 and PM10.We are processing the data before sending it to the network. ")
