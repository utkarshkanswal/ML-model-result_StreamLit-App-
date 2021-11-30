from numpy import loadtxt
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
n = 25

particle = ['NO2', 'O3', 'NO', 'CO', 'PM1', 'PM2.5', 'PM10']


def actual_vs_predicted():
    select_model = st.sidebar.radio(
        "Choose Model ?", ('Xgboost', 'Randomforest', 'KNN'))

    select_particle = st.sidebar.radio(
        "Choose Particle ?", ('NO2', 'O3', 'NO', 'CO', 'PM1', 'PM2.5', 'PM10'))

    if select_particle == 'NO2':
        loc = 0
    if select_particle == 'O3':
        loc = 1
    if select_particle == 'NO':
        loc = 2

    if select_particle == 'CO':
        loc = 3

    if select_particle == 'PM1':
        loc = 4

    if select_particle == 'PM2.5':
        loc = 5

    if select_particle == 'PM10':
        loc = 6

    if select_model == 'Xgboost':
        get_xgboost(loc)
    if select_model == 'KNN':
        get_knn(loc)

    if select_model == 'Randomforest':
        get_randomforest(loc)


def get_knn(loc):

    knn_y_test = loadtxt('Models/knn_y_test.csv', delimiter=',')
    knn_y_test_pred = loadtxt('Models/knn_y_test_pred.csv', delimiter=',')
    l1 = list()
    l1.append(['Y_Actual']*n)
    l1.append(np.round(knn_y_test[:n, loc], 9))
    l1.append(list(range(1, n+1)))
    temp1 = np.array(l1).transpose()
    x1 = list(range(1, n+1))

    chart_data1 = pd.DataFrame(temp1, x1, columns=['Data', particle[loc], 'x'])

    l2 = list()
    l2.append(['Y_Predicted']*n)
    l2.append(np.round(knn_y_test_pred[:n, loc], 9))
    l2.append(list(range(1, n+1)))
    temp2 = np.array(l2).transpose()
    x2 = list(range(n+1, 2*n+1))

    chart_data2 = pd.DataFrame(temp2, x2, columns=['Data', particle[loc], 'x'])

    frames = [chart_data1, chart_data2]

    results = pd.concat(frames)

    chart = alt.Chart(results).mark_line().encode(
        x='x',
        y=particle[loc],
        color='Data',
        strokeDash='Data',
    ).properties(
        title='Plot of Actual vs Predicted for KNN model for ' +
        particle[loc]+' particle'
    )
    st.altair_chart(chart, use_container_width=True)


def get_xgboost(loc):

    xgboost_y_test = loadtxt('Models/xgboost_y_test.csv', delimiter=',')
    xgboost_y_test_pred = loadtxt(
        'Models/xgboost_y_test_pred.csv', delimiter=',')
    l1 = list()
    l1.append(['Y_Actual']*n)
    l1.append(np.round(xgboost_y_test[:n, loc], 9))
    l1.append(list(range(1, n+1)))
    temp1 = np.array(l1).transpose()
    x1 = list(range(1, n+1))

    chart_data1 = pd.DataFrame(temp1, x1, columns=['Data', particle[loc], 'X'])

    l2 = list()
    l2.append(['Y_Predicted']*n)
    l2.append(np.round(xgboost_y_test_pred[:n, loc], 9))
    l2.append(list(range(1, n+1)))
    temp2 = np.array(l2).transpose()
    x2 = list(range(n+1, 2*n+1))

    chart_data2 = pd.DataFrame(temp2, x2, columns=['Data', particle[loc], 'X'])

    frames = [chart_data1, chart_data2]

    results = pd.concat(frames)

    chart = alt.Chart(results.reset_index()).mark_line().encode(
        x='X',
        y=particle[loc],
        color='Data',
        strokeDash='Data',
    ).properties(
        title='Plot of Actual vs Predicted for Xgboost model for ' +
        particle[loc]+' particle'
    )
    st.altair_chart(chart, use_container_width=True)


def get_randomforest(loc):

    xgboost_y_test = loadtxt('Models/randomforest_y_test.csv', delimiter=',')
    xgboost_y_test_pred = loadtxt(
        'Models/randomforest_y_test_pred.csv', delimiter=',')
    l1 = list()
    l1.append(['Y_Actual']*n)
    l1.append(np.round(xgboost_y_test[:n, loc], 9))
    l1.append(list(range(1, n+1)))
    temp1 = np.array(l1).transpose()
    x1 = list(range(1, n+1))

    chart_data1 = pd.DataFrame(temp1, x1, columns=['Data', particle[loc], 'X'])

    l2 = list()
    l2.append(['Y_Predicted']*n)
    l2.append(np.round(xgboost_y_test_pred[:n, loc], 9))
    l2.append(list(range(1, n+1)))
    temp2 = np.array(l2).transpose()
    x2 = list(range(n+1, 2*n+1))

    chart_data2 = pd.DataFrame(temp2, x2, columns=['Data', particle[loc], 'X'])

    frames = [chart_data1, chart_data2]

    results = pd.concat(frames)

    chart = alt.Chart(results.reset_index()).mark_line().encode(
        x='X',
        y=particle[loc],
        color='Data',
        strokeDash='Data',
    ).properties(
        title='Plot of Actual vs Predicted for Randomforest model for ' +
        particle[loc]+' particle'
    )
    st.altair_chart(chart, use_container_width=True)
