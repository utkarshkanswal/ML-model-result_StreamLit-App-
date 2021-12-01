from logging import error
import streamlit as st
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import altair as alt

data_type = ['Test Data', 'Train Data']

xgboost_list = [0.7867491776691122, 0.804894044676069]
randomforest_list = [0.6329507787480243, 0.6406985506761919]
Linear_regression_list = [0.2929796878382063, 0.2948116798857159]
Lasso_list = [-8.30655766355311e-06, 3.407978172024928e-12]
knn_list = [0.7463683061096252, 0.8164847956978979]


def r2_scorepj():
    st.sidebar.subheader("Choose Model ?")
    select_model1 = st.sidebar.checkbox('Xgboost')
    select_model2 = st.sidebar.checkbox('Random Forest')
    select_model3 = st.sidebar.checkbox('Linear Regression')
    select_model4 = st.sidebar.checkbox('Lasso')
    select_model6 = st.sidebar.checkbox('K Nearest Neighbour')

    models = list()
    arr = list()

    if select_model1:
        arr.append(xgboost_list)
        models.append("Xgboost")

    if select_model2:
        arr.append(randomforest_list)
        models.append("Random Forest")

    if select_model3:
        arr.append(Linear_regression_list)
        models.append("Linear Regression")

    if select_model4:
        arr.append(Lasso_list)
        models.append("Lasso")

    if select_model6:
        arr.append(knn_list)
        models.append("KNN")

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
