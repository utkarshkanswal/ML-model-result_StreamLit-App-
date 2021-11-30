import streamlit as st
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import altair as alt
import math

xgboost_list = [9.53231e-06, 0.0008703509, 0.003087444]
randomforest_list = [5.4943812238677005e-05,
                     0.0021928648657524178, 0.0074124093410089685]
linear_regression_list = [0.14759162,0.0039615664,0.38417655]
Lasso_list = [0.00013819191,0.0043099066,0.011755506]
linear_regressionmax_list = [0.00012164231712440681, 0.007302540667162326,
               0.011029157589063945, -3622904.383916931, -3621361.2122283005]
knn_list = [4.8233207e-05, 0.0018312254, 0.006945013]
svm_list = [0.0050151326902311095, 0.06570361499714113, 0.07081760155661239]
lstm = [2.0402e-04, 0.0098, 0.0122]


def error_anaysis():
    st.sidebar.subheader("Choose Model ?")
    select_model1 = st.sidebar.checkbox('Xgboost')
    select_model2 = st.sidebar.checkbox('Random Forest')
    select_model3 = st.sidebar.checkbox('Linear Regression')
    select_model4 = st.sidebar.checkbox('Lasso')
    # select_model5 = st.sidebar.checkbox(
    #     'Vector Auto Regression Moving Average')
    select_model6 = st.sidebar.checkbox('K Nearest Neighbour')
    # select_model7 = st.sidebar.checkbox('Support Vector Machine')
    # select_model8 = st.sidebar.checkbox('LSTM')
    models = list()

    if select_model1:
        models.append("Xgboost")

    if select_model2:
        models.append("Random Forest")

    if select_model3:
        models.append("Linear Regression")

    if select_model4:
        models.append("Lasso")

    # if select_model5:
    #     models.append("linear_regressionMA")

    if select_model6:
        models.append("KNN")

    # if select_model7:
    #     models.append("SVM")

    # if select_model8:
    #     models.append("LSTM")

    st.sidebar.subheader("Choose Value ?")

    select_error2 = st.sidebar.checkbox('Mean Squared Error (MSE)')
    select_error3 = st.sidebar.checkbox('Mean Absolute Error (MAE)')
    select_error4 = st.sidebar.checkbox('Root Mean Squared Error (RMSE)')

    errors = list()

    if select_error2:
        errors.append("MSE")

    if select_error3:
        errors.append("MAE")

    if select_error4:
        errors.append("RMSE")

    arr = list()
    for m in models:
        l = list()
        for e in errors:
            if e == "MSE" and m == "Xgboost":
                l.append(xgboost_list[0])
            if e == "MAE" and m == "Xgboost":
                l.append(xgboost_list[1])
            if e == "RMSE" and m == "Xgboost":
                l.append(xgboost_list[2])
            if e == "MSE" and m == "Random Forest":
                l.append(randomforest_list[0])
            if e == "MAE" and m == "Random Forest":
                l.append(randomforest_list[1])
            if e == "RMSE" and m == "Random Forest":
                l.append(randomforest_list[2])
            if e == "MSE" and m == "Linear Regression":
                l.append(linear_regression_list[0])
            if e == "MAE" and m == "Linear Regression":
                l.append(linear_regression_list[1])
            if e == "RMSE" and m == "Linear Regression":
                l.append(linear_regression_list[2])
            if e == "MSE" and m == "Lasso":
                l.append(Lasso_list[0])
            if e == "MAE" and m == "Lasso":
                l.append(Lasso_list[1])
            if e == "RMSE" and m == "Lasso":
                l.append(Lasso_list[2])
            if e == "MSE" and m == "linear_regressionMA":
                l.append(linear_regressionmax_list[0])
            if e == "MAE" and m == "linear_regressionMA":
                l.append(linear_regressionmax_list[1])
            if e == "RMSE" and m == "linear_regressionMA":
                l.append(linear_regressionmax_list[2])
            if e == "MSE" and m == "KNN":
                l.append(knn_list[0])
            if e == "MAE" and m == "KNN":
                l.append(knn_list[1])
            if e == "RMSE" and m == "KNN":
                l.append(knn_list[2])
            if e == "MSE" and m == "SVM":
                l.append(svm_list[0])
            if e == "MAE" and m == "SVM":
                l.append(svm_list[1])
            if e == "RMSE" and m == "SVM":
                l.append(svm_list[2])
            if e == "MSE" and m == "LSTM":
                l.append(lstm[0])
            if e == "MAE" and m == "LSTM":
                l.append(lstm[1])
            if e == "RMSE" and m == "LSTM":
                l.append(lstm[2])

        arr.append(l)

    temp = np.array(arr).transpose()

    if len(models) > 0 and len(errors) > 0:
        st.header("Plot for Different Errors for different Models")
        chart_data = pd.DataFrame(temp, errors, columns=models)
        st.table(chart_data)
        st.line_chart(chart_data, height=450)
    else:
        title = st.title("Welcome to Air Quality Result Analysis Web App")
        st.markdown("Comparative analysis on dataset of different machine learning models  and find out the best model having more accurate predictions of air quality .")
        st.markdown("The dataset is a collection of sensor data for 7 different locations of Malaysia which is collected through OPC sensors. These data are for 15 months that are from March 2019 to May 2020. These data are in CSV or Excel files. These data are saved in month wise format. These data have 57 columns and 35847 rows. These data are recorded for every hour.")
        st.markdown("For the sensor data, out of these 57 features(i.e. number of columns) we are taking 5 features as our input target and 7 as our output target. The input targets are Node value, date, time, external temperature and external RH. The output targets are NO2 ppb, O3 ppb, NO ppb, CO ppb, PM1, PM2.5 and PM10.We are processing the data before sending it to the network. ")
