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


title = st.title("Welcome to Air Quality Result Analysis Web App")


st.sidebar.subheader("Choose Model ?")
select_model1 = st.sidebar.checkbox('Xgboost')
select_model2 = st.sidebar.checkbox('Random Forest')
select_model3 = st.sidebar.checkbox('Vector Auto Regression')
select_model4 = st.sidebar.checkbox('Vector Moving Average')
select_model5 = st.sidebar.checkbox('Vector Auto Regression Moving Average')

models = list()

if select_model1:
    models.append("Xgboost")

if select_model2:
    models.append("Random Forest")

if select_model3:
    models.append("VAR")

if select_model4:
    models.append("VMA")

if select_model5:
    models.append("VMA")

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
j = 0
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
        if e == "MSE" and m == "VAR":
            l.append(var_list[0])
        if e == "MAE" and m == "VAR":
            l.append(var_list[1])
        if e == "RMSE" and m == "VAR":
            l.append(var_list[2])
        if e == "MSE" and m == "VMA":
            l.append(vma_list[0])
        if e == "MAE" and m == "VMA":
            l.append(vma_list[1])
        if e == "RMSE" and m == "VMA":
            l.append(vma_list[2])
        if e == "MSE" and m == "VARMA":
            l.append(varmax_list[0])
        if e == "MAE" and m == "VARMA":
            l.append(varmax_list[1])
        if e == "RMSE" and m == "VARMA":
            l.append(varmax_list[2])
        j += 1

    arr.append(l)

temp = np.array(arr).transpose()

if len(models) > 0 and len(errors) > 0:
    st.subheader("Plot for different errors for different models")
    chart_data = pd.DataFrame(temp, errors, columns=models)
    st.line_chart(chart_data, height=450)
