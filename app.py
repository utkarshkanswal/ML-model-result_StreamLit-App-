import streamlit as st
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import altair as alt
from error_analysis import error_anaysis
from r2_score import r2_score
from aic_bic import aic_bic_anaysis

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


t = st.sidebar.radio(
    'Choose One ?', ('Error Analysis', 'R2 Score', 'AIC and BIC'))

if t == "Error Analysis":
    error_anaysis()
elif t == "R2 Score":
    r2_score()
elif t == "AIC and BIC":
    aic_bic_anaysis()
