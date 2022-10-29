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
#from streamlit_option_menu import option_menu
# streamlit run dash.py
import pandas as pd
import numpy as np
import pickle

# data vis
#import plotly.express as px

from dateutil.relativedelta import relativedelta
import math


# setting a wide layout
st.set_page_config(page_title="Tweets", layout="wide")

# columns
header = st.container()
#col1, col2 = st.columns(2)
#page2 = st.container()
#dataset = st.container()
#features = st.container()
# import pickle file
st.title("Prediction of Ice cream shop revenue")
st.markdown(
    "Here we are using temperature as the input to predict the day's revenue")


# df_csv = pd.read_csv(
# "https://raw.githubusercontent.com/RitRa/Msc_sentiment_analysis/main/data/ukgov_23.csv", encoding='latin-1')
# df_csv

df_new = pickle.load(open('../data/data.pkl', 'rb'))

df_new
