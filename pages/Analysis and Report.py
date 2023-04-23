# Contents of ~/my_app/pages/page_2.py
import time

import streamlit as st
import pandas as pd
import numpy as np
import datetime
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
from os import path
import os
from collections import Counter
import json
import openai

openai.api_key = ""

st.set_page_config(page_title="Analysis & Report",
                   page_icon=":guardsman:", layout="wide")


d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
assets = path.join(path.dirname(d), "assets")


def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")


def read_json(file):
    f = open(file, "r")
    data = json.load(f)
    f.close()
    return data


def produce_sentiment_df(org_df):
    line_chart_date = sorted(list(set(org_df["date"])))
    d = []
    for day in line_chart_date:
        df1 = org_df[org_df["date"] == day]
        try:
            positive = int(df1[df1["sentiment"] == "positive"].groupby(by=["date"]).count()["sentiment"])
        except:
            positive = 0
        try:
            negative = int(df1[df1["sentiment"] == "negative"].groupby(by=["date"]).count()["sentiment"])
        except:
            negative = 0
        try:
            neutral = int(df1[df1["sentiment"] == "neutral"].groupby(by=["date"]).count()["sentiment"])
        except:
            neutral = 0
        line = dict()
        line["date"] = day
        line["positive"] = positive / (positive + negative + neutral)
        line["negative"] = negative / (positive + negative + neutral)
        line["neutral"] = neutral / (positive + negative + neutral)
        d.append(line)
    return pd.DataFrame(d)


def produce_overall_sentiment_layout(org_df):
    try:
        positive = int(org_df[org_df["sentiment"] == "positive"].count()["sentiment"])
    except:
        positive = 0
    try:
        negative = int(org_df[org_df["sentiment"] == "negative"].count()["sentiment"])
    except:
        negative = 0
    try:
        neutral = int(org_df[org_df["sentiment"] == "neutral"].count()["sentiment"])
    except:
        neutral = 0
    return positive, negative, neutral


st.subheader("Sentiment Analysis and Report ❄️")
st.markdown("We will filter the collected LA data according to the time and topic you choose, "
            "and dynamically generate all the tables, charts and pictures below")

# read the original json into this project
original_df = pd.DataFrame(read_json(path.join(assets, "new_reddit.json")))
# get the start date and the final date
date = sorted(list(set(original_df["date"])))

# set the time span for the customer to choose the time
start_year, start_month, start_day = date[0].split('-')
end_year, end_month, end_day = date[-1].split('-')
start_time, end_time = datetime.date(int(start_year), int(start_month), int(start_day)), \
                       datetime.date(int(end_year), int(end_month), int(end_day))
# get the selected time span (s, e)
s, e = st.slider(
    "Please select a time range you are interested in:",
    value=(start_time, end_time))

# show it
st.write("Start time:", s)
st.write("End time:", e)


# Choose the topic
options = st.multiselect(
    'Which topic are you focusing on?',
    ['All', 'affordable housing', 'crime', 'homeless', 'traffic', 'water supply'],
    ['All'])


# Choose the cities
# cities = st.multiselect(
#     'Which topic are you focusing on?',
#     ['All', 'Los Angeles', 'Torrance', 'Santa Monica', 'Pasadena', 'Long Beach', 'Culver City'],
#     ['All'])


def filter_dataframe(df, start, end, topic):
    filter1 = df[df["date"] > str(start)]
    filter2 = filter1[filter1["date"] < str(end)]
    if "All" in topic:
        return filter2
    df_set = []
    for t in topic:
        ft = filter2[filter2["topic"] == t]
        df_set.append(ft)
    return pd.concat(df_set)


def filter_city(df, city):
    data = df[df["city"] == city]
    return data


filtered_df = filter_dataframe(original_df, s, e, options)

diff_city_df_set = []
# if "All" not in cities:
#     for city in cities:
#         data = filter_city(filtered_df, city)
#         diff_city_df_set.append(data)


st.subheader("Data table display️")
st.markdown("By cleaning and processing the collected social media data, "
            "the table below shows the results of our sentiment analysis and keyword extraction on text data")
st.dataframe(filtered_df)

# blank line
space(1)
st.markdown("---")
space(2)

# line chart
st.subheader("Trends in Public's Sentiment towards City Services")
st.markdown("The line chart below shows the sentiment curve of the people of LA under the selected time and topics")

# blank line
space(2)


def product_chart_data(df):
    sentiment_df = produce_sentiment_df(df)
    chart_data = sentiment_df[["positive", "negative", "neutral"]]
    chart_data.index = sorted(list(sentiment_df["date"]))
    return chart_data


if not diff_city_df_set:
    chart_data = product_chart_data(filtered_df)
    # Description: This is a simple streamlit app that displays a line chart
    st.line_chart(chart_data)
    overall_positive, overall_negative, overall_neutral = produce_overall_sentiment_layout(filtered_df)
    st.write("Overall Positive Rate: ", overall_positive / (overall_positive + overall_negative + overall_neutral))
    st.write("Overall Negative Rate: ", overall_negative / (overall_positive + overall_negative + overall_neutral))
    st.write("Overall Neutral Rate: ", overall_neutral / (overall_positive + overall_negative + overall_neutral))

# else:
#     for index, city_df in enumerate(diff_city_df_set):
#         st.write("The following line chart represent city :", cities[index])
#         chart_data = product_chart_data(city_df)
#         st.line_chart(chart_data)


st.markdown("---")

space(2)

st.subheader("Word Cloud")
st.markdown("By using the keywords summarized in the table above, we generated the following word cloud")

cloud_mask = np.array(Image.open(path.join(assets, "cloud.png")))


# text holder
def generate_word_cloud(df):
    text = ""
    keyword_list = list(df["keyword"])
    keyword_all_set = []
    for keywords in keyword_list:
        for keyword in keywords:
            text += " " + str(keyword)
            keyword_all_set.append(keyword)
    # Create the word cloud
    word_cloud = WordCloud(background_color='white', max_font_size=100, mask=cloud_mask).generate(text)
    return word_cloud, Counter(keyword_all_set)


# Display the word cloud using matplotlib
fig, ax = plt.subplots()
wc, counter = generate_word_cloud(filtered_df)
ax.imshow(wc, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)


def chatgpt_answer(user_query):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "user", "content": user_query}],
        max_tokens=193,
        temperature=0,
    )

    return response["choices"][0]["message"]["content"]


def generate_latent_problems(counter):
    text = "The following paragraph shows the number of occurrences of " \
           "each word, Can you guess less than 10 possible urban problems based on the words " \
           "that appear? Please only list the name of each problem and use comma to split."
    word_cnt = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    word_cnt = word_cnt[:30] if len(word_cnt) > 30 else word_cnt
    for word, cnt in word_cnt:
        text += " " + word + ": " + str(cnt) + ","

    latent_problems = chatgpt_answer(text)
    print(latent_problems)
    problem_dict = dict()
    problem_dict["questions"] = dict()
    for problem in latent_problems.split(','):
        base_t = "Can you give me a basic suggestion to solve the problem of " + \
                 problem + ". Please use less than 200 words to conclude."
        basic_solution = chatgpt_answer(base_t)
        problem_dict["questions"][problem] = basic_solution
    problem_dict["time"] = time.time()

    with open(path.join(assets, "generated_questions.json"), "w") as f:
        json.dump(problem_dict, f, indent=2)


# generate_latent_problems(counter)