# Contents of ~/my_app/pages/page_3.py
import json
import time

import streamlit as st
import openai
from streamlit_chat import message
import os
from os import path

st.set_page_config(page_title="Latent problems & solution",
                   page_icon=":guardsman:", layout="wide")

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
assets = path.join(path.dirname(d), "assets")

openai.api_key = ""


def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")


# ----------------------------------  latent problems ----------------
def display_answer(question):
    answer = questions[question]
    st.write(answer)


def read_json(file):
    f = open(file, "r")
    data = json.load(f)
    f.close()
    return data


header_text = "Here are the potential problems discovered from social media data, " \
              "click to see how ChatGPT addresses those problems."

st.subheader(header_text)


# Define the questions and answers
generated_json_path = path.join(assets, "generated_questions.json")
if not os.path.exists(generated_json_path):
    questions = read_json(path.join(assets, "initial_questions.json"))
else:
    generated_json = read_json(generated_json_path)
    passed_time = time.time() - float(generated_json["time"])
    if passed_time < 60:
        questions = generated_json["questions"]
    else:
        questions = read_json(path.join(assets, "initial_questions.json"))
# print(questions)


# Create a list of clickable question titles
question_titles = [q for q in questions.keys()]


t = ""
# Display the questions and answers
for title in question_titles:
    # Add a clickable question title
    if st.button(title):
        # Display the answer when the question title is clicked
        display_answer(title)
        t = title
        st.session_state['generated'] = []
        st.session_state['past'] = []


# ----------------------------- chat box --------------------------------
def get_text():
    input_text = st.text_input("You: ", t, key="input")
    return input_text


def chatgpt_answer(user_query):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_query,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip('\n')


# blank line
space(1)
st.markdown("---")
space(1)

# Creating the chatbot interface
st.subheader("Hi : Ask GPT if you have further questions.")

user_input = get_text()

# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

if user_input:
    # output = chatgpt_answer(user_input)
    output = "hahaha"
    # store the output
    st.session_state['past'].append(user_input)
    st.session_state['generated'].append(output)

# Displaying the chat
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i],
                key=str(i),
                avatar_style="adventurer",
                seed=560)
        message(st.session_state['past'][i],
                is_user=True, key=str(i) + '_user')