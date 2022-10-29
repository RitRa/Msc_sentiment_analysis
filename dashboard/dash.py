# install the following packages
# pip install streamlit
# pip install plotly

# Run file
# make sure you are in the working directory of the streamlit file
# streamlit run dash.py

# Add dependencies
# pip freeze > requirements.txt

import requests
from io import BytesIO
import streamlit as st
# from streamlit_option_menu import option_menu
# streamlit run dash.py
import pandas as pd
import numpy as np
import pickle
import os
from plotly import graph_objs as go

# data vis
import plotly.express as px

from dateutil.relativedelta import relativedelta
import math


# setting a wide layout
st.set_page_config(page_title="Tweets", layout="wide")

# columns
header = st.container()
# col1, col2 = st.columns(2)
# page2 = st.container()
# dataset = st.container()
# features = st.container()
# import pickle file
st.title("Prediction of sentiment")
st.markdown("Sentiment analysis for UK Gov")


pickle_xgb = open(
    '/app/msc_sentiment_analysis/dashboard/forecasterxgb.pkl', 'rb')
pickle_df = open(
    '/app/msc_sentiment_analysis/dashboard/df_cmp.pkl', 'rb')
# pickle_xgb = open(
#     'forecasterxgb.pkl', 'rb')
regressor_xgb = pickle.load(pickle_xgb)


# pickle_df = open(
#     'df_cmp.pkl', 'rb')
df_cmp = pickle.load(pickle_df)


# df_cmp
# regressor_xgb

steps = 30

data_train = df_cmp[:-steps]
data_test = df_cmp[-steps:]

# choice of steps
step = {'90 days': 90,
        '60 days': 60,
        '30 days': 30,
        '7 days': 7}


# dropdown timeframe for model
select_timeframe = st.selectbox(
    'Select timeframe:', ("7 days", "30 days", "60 days", "90 days"))

# st.write('You selected:', select_timeframe)


#predictions = regressor_xgb.predict(steps=steps)

# predictions

def evaluate_model(select_timeframe, step, regressor_xgb):
    for key, value in step.items():

        if select_timeframe == key:
            # applies the steps from the user input to the model
            predictions = regressor_xgb.predict(steps=value)
            # predictions
            #st.write("rita this is a test", key, value)
            #
            st.write("step:", value)

            test_data = pd.DataFrame({
                'Predicted': predictions,                       # Test Predict Data
                'Test': data_test['compound_daily']
            })
            # plot
            fig_new = px.line(test_data)
            # streamlit call
            st.plotly_chart(fig_new, use_container_width=True)

            full_data = pd.DataFrame({
                'Predicted': predictions,                       # Test Predict Data
                # Test Actual Data
                'Test': data_test['compound_daily'],
                # Test Actual Data
                'Train': data_train['compound_daily']
            })

            fig_full = px.line(full_data)                        # plot
            # streamlit call
            st.plotly_chart(fig_full, use_container_width=True)


evaluate_model(select_timeframe, step, regressor_xgb)

#######################
