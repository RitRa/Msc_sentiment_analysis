# install the following packages
# pip install streamlit
# pip install plotly

# Run file
# make sure you are in the working directory of the streamlit file
# streamlit run dash.py

# Add dependencies
# pip freeze > requirements.txt


############################# Libraries start #############################
#import requests
#from io import BytesIO
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
import plotly.express as px

#from dateutil.relativedelta import relativedelta
#import math

############################# Libraries end #############################


# setting a wide layout
st.set_page_config(page_title="Models",
                   page_icon="👋",
                   layout="wide"
                   )

# columns
# st.sidebar.markdown("# Models Evaluation")
#header = st.container()

# col1, col2 = st.columns(2)
# page2 = st.container()
# dataset = st.container()
model_evaluation = st.container()


############################# Data start #############################
# import pickle file
pickle_xgb = open(
    '/app/msc_sentiment_analysis/dashboard/forecasterxgb.pkl', 'rb')
pickle_df = open(
    '/app/msc_sentiment_analysis/dashboard/df_cmp.pkl', 'rb')
# pickle_xgb = open(
#     './forecasterxgb.pkl', 'rb')
# regressor_xgb = pickle.load(pickle_xgb)


# pickle_df = open(
#     './df_cmp.pkl', 'rb')
# df_cmp = pickle.load(pickle_df)
############################# Data end #############################


############################# Model Eval start #############################
with model_evaluation:
    st.title("Model Evaluation")
    st.write("Select a timeframe to analysis sentiment")
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

                st.write("step:", value)
                st.write("Regressor: XGBRegressor")

                test_data = pd.DataFrame({
                    'Predicted': predictions,                       # Test Predict Data
                    'Test': data_test['compound_daily']

                })
                # plot
                fig_new = px.line(
                    test_data, title="Predicted data vs test data using %s" % (value))
                # streamlit call
                st.plotly_chart(fig_new, use_container_width=True)

                full_data = pd.DataFrame({
                    'Predicted': predictions,                       # Test Predict Data
                    # Test Actual Data
                    'Test': data_test['compound_daily'],
                    # Test Actual Data
                    'Train': data_train['compound_daily']
                })

                fig_full = px.line(full_data, title="Actual Vs Predicted using %s" % (
                    value))                        # plot
                # streamlit call
                st.plotly_chart(fig_full, use_container_width=True)

    evaluate_model(select_timeframe, step, regressor_xgb)

############################# Model Eval end #############################
