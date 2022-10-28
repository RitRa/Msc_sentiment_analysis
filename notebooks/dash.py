import streamlit as st
#from streamlit_option_menu import option_menu
#streamlit run dashboard.py
import pandas as pd
import numpy as np
import pickle

#data vis
import plotly.express as px

from dateutil.relativedelta import relativedelta
import math


#setting a wide layout
st.set_page_config(page_title="Tweets", layout="wide")

#columns
#header = st.container()
#col1, col2 = st.columns(2)
#page2 = st.container()
#dataset = st.container()
#features = st.container()


#tweets
filename ="https://raw.githubusercontent.com/RitRa/Msc_sentiment_analysis/master/data/df.pkl"
infile = open(filename,'rb')
df = pickle.load(infile)


df.head(5)
