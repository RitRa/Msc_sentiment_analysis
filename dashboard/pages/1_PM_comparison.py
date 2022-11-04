############################# Libraries start #############################
from PIL import Image
import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os
import plotly.express as px

############################# Libraries end #############################

############################# Data start #############################
df_all = open(
    '/app/msc_sentiment_analysis/dashboard/df_full.pkl', 'rb')

boris_image = '/app/msc_sentiment_analysis/dashboard/img/boris.jpeg'
liz_image = '/app/msc_sentiment_analysis/dashboard/img/liz.jpeg'
rishi_image = '/app/msc_sentiment_analysis/dashboard/img/rishi.jpeg'

# df_all = open(
#     './df_full.pkl', 'rb')
df = pickle.load(df_all)

# boris_image = './img/boris.jpeg'
# liz_image = './img/liz.jpeg'
# rishi_image = './img/rishi.jpeg'

image_boris = Image.open(boris_image)
image_liz = Image.open(liz_image)
image_rishi = Image.open(rishi_image)

############################# Data start #############################

st.markdown("# Prime Minister sentiment comparison ❄️")
# st.sidebar.markdown("# Page 2 ❄️")

boris_section = st.container()
liz_section = st.container()
rishi_section = st.container()

col1, col2 = st.columns((1, 5))

df_boris = df[df['tweet_clean'].str.contains("boris", case=False)]
df_liz = df[df['tweet_clean'].str.contains("liz", case=False)]
df_rishi = df[df['tweet_clean'].str.contains("rishi", case=False)]

with boris_section:

    with col1:
        st.subheader('Boris')

        st.image(image_boris, caption="Boris Johnson", width=None,  use_column_width=None,
                 clamp=False, channels="RGB", output_format="auto")

        st.write("Boris saw a raise in his median compound score in Q4 2022")

    with col2:

        fig_box = px.box(df_boris, x='quarter', y='compound', color="Year")
        fig_box.update_layout(height=400)
        # disply line Chart
        st.plotly_chart(fig_box, use_container_width=True)

with liz_section:

    with col1:
        st.subheader('Liz')
        st.image(image_liz, caption=None, width=None, use_column_width=None,
                 clamp=False, channels="RGB", output_format="auto")
        st.write("Looking back at the Liz's compound score for the year of 2022,  her median score was mostly negative and then very neutral for q3 and q4 2022")

    with col2:
        fig_box = px.box(df_liz, x='quarter', y='compound', color="Year")
        fig_box.update_layout(height=400)
        # disply line Chart
        st.plotly_chart(fig_box, use_container_width=True)


with rishi_section:

    with col1:
        st.subheader('Rishi')
        st.image(image_rishi, caption=None, width=None, use_column_width=None,
                 clamp=False, channels="RGB", output_format="auto")
        st.write("Looking back at Rishi's compound score for 2022, his median score was very positive and now again in Q4 we is enjoying a very high sentiment score indeed")
    with col2:
        fig_box = px.box(df_rishi, x='quarter', y='compound',
                         title='Rishi Sunak sentiment by Quarter', color="Year")
        fig_box.update_layout(height=500)

        # disply line Chart
        st.plotly_chart(fig_box, use_container_width=True)
