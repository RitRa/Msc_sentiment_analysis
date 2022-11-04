# install the following packages
# pip install streamlit
# pip install plotly

# Run file
# make sure you are in the working directory of the streamlit file
# streamlit run dash.py

# Add dependencies
# pip freeze > requirements.txt


############################# Libraries start #############################
# import requests
# from io import BytesIO
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
import plotly.express as px

# from dateutil.relativedelta import relativedelta
# import math

############################# Libraries end #############################


# setting a wide layout
st.set_page_config(page_title="Home",
                   page_icon="👋",
                   layout="wide"
                   )


home_page = st.container()
col1, col2 = st.columns((1, 4))

############################# Data start #############################
# import pickle file
pickle_xgb = open(
    '/app/msc_sentiment_analysis/dashboard/forecasterxgb.pkl', 'rb')
pickle_df = open(
    '/app/msc_sentiment_analysis/dashboard/df_cmp.pkl', 'rb')

full_df = open(
    '/app/msc_sentiment_analysis/dashboard/df_full.pkl', 'rb')


# pickle_xgb = open(
#     'forecasterxgb.pkl', 'rb')
# regressor_xgb = pickle.load(pickle_xgb)


# pickle_df = open(
#     'df_cmp.pkl', 'rb')
# df_cmp = pickle.load(pickle_df)


# full_df = open(
#     'df_full.pkl', 'rb')
# df_full = pickle.load(full_df)
############################# Data end #############################


############################# Model Eval start #############################
with home_page:
    st.subheader('Home')

    df_full.describe()

    fig_box = px.histogram(df_full, x='compound',
                           title="Sentiment: Compound from Tweets about UKGOV")
    fig_box.update_layout(height=400)
    # disply line Chart
    st.plotly_chart(fig_box, use_container_width=True)

    st.subheader("Top tweeters about 'ukgov'")
with col1:

    top_tweeters = df_full['Username'].value_counts().nlargest(10)
    top_tweeters
with col2:
    fig2 = px.bar(top_tweeters)
    st.plotly_chart(fig2, use_container_width=True)
