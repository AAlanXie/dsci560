# Contents of ~/my_app/pages/page_2.py
import streamlit as st
import pandas as pd
import numpy as np
import datetime
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
from os import path
import os

# blank line


def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")


st.markdown("# Sentiment Analysis and Report ❄️")


df = pd.DataFrame(
   np.random.randn(100, 8),
   columns=("Date", "original text", "positive", "negative", "neutral", "keyword", "category", "summarization")
)

st.dataframe(df)


# line chart
st.markdown("# Trends in Public's Sentiment towards City Services")

start_time, end_time = datetime.date(2020, 1, 1), datetime.date(2021, 1, 1)
s, e = st.slider(
    "Please select a time range:",
    value=(start_time, end_time))


st.write("Start time:", s)
st.write("End time:", e)

options = st.multiselect(
    'Which topic are you focusing on?',
    ['All', 'Transportation', 'Security', 'Waste Management'],
    ['All'])

# blank line
space(2)

st.markdown("---")

space(2)


chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['positive', 'negative', 'neutral'])

# Description: This is a simple streamlit app that displays a line chart
st.line_chart(chart_data)


# blank line
space(2)

st.markdown("---")

space(2)

st.subheader("Word Cloud")
st.markdown("# Word Cloud")
st.markdown("## Extract the most frequent keywords used on social media in the past 7 days")

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
assets = path.join(path.dirname(d), "assets")
cloud_mask = np.array(Image.open(path.join(assets, "cloud.png")))

# text holder
text = "Trash pickup, street cleaning, public transportation, police department, fire department, parks and recreation, public library, animal control, building permits, zoning regulations, parking enforcement, emergency services, community centers, water and sewer services, public schools, public health services, city government, public works, snow removal, code enforcement, public transportation, public health services, street cleaning, animal control, public works, public schools, parks and recreation, emergency services"

# Create the word cloud
wordcloud = WordCloud(mask=cloud_mask).generate(text)

# Display the word cloud using matplotlib
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)
