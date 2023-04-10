# Contents of ~/my_app/pages/page_3.py
import streamlit as st
import openai
import os
from streamlit_chat import message

openai.api_key = ""

t = ""


def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")


# ----------------------------------  latent problems ----------------
def display_answer(question):
    answer = questions[question]
    st.write(answer)


header_text = "Here are the potential problem discover from social media data, " \
              "click to see how ChatGPT addresses those problems."
st.subheader(header_text)
# Define the questions and answers
questions = {
    "Problem 1: Traffic congestion": "Implement and expand public transportation options such as buses, subways, and light rail to encourage residents to use public transit instead of driving alone. Encourage carpooling and provide incentives for employers to implement flexible work schedules to reduce the number of cars on the road during peak traffic hours. Invest in smart traffic management systems to optimize traffic flow and reduce congestion.",

    "Problem 2: Potholes and road damage": "Prioritize road maintenance and repair by allocating sufficient budget and resources to the Department of Public Works. Conduct regular inspections and repairs to ensure road safety and prevent costly repairs in the future. Encourage residents to report road damage through the MyLA311 app or hotline to ensure prompt repairs.",

    "Problem 3: Trash collection issues": "Educate residents on proper waste disposal practices and encourage them to sort trash and recyclables correctly to reduce contamination and improve collection efficiency. Increase trash collection frequency in high-density areas to reduce overflow and illegal dumping. Invest in waste-to-energy technology to reduce landfill waste and generate clean energy.",

    "Problem 4: Power outages": "Invest in upgrading and modernizing the city's power grid to improve reliability and reduce the risk of outages. Increase the use of renewable energy sources such as solar and wind power to reduce dependence on fossil fuels and improve energy resilience. Encourage residents to conserve electricity during peak demand periods to reduce strain on the power grid.",

    "Problem 5: Street cleaning violations": "Improve signage and communication to ensure residents are aware of street cleaning schedules and restrictions. Increase street cleaning frequency in high-traffic areas to prevent litter buildup and maintain cleanliness. Enforce parking violations with clear penalties to discourage violations and ensure compliance with street cleaning regulations.",

    "Problem 6: Graffiti": "Invest in programs and initiatives to prevent graffiti and provide resources for prompt removal. Encourage community involvement in reporting and removing graffiti through neighborhood watch programs and community cleanup events. Increase penalties for graffiti offenders to deter future vandalism.",

    "Problem 7: Noise complaints": "Enforce noise regulations with clear penalties and consequences for violators. Increase community awareness of noise regulations through education and outreach programs. Work with businesses and residents to reduce noise pollution and promote a more peaceful and livable city.",

    "Problem 8: Homelessness": "Invest in affordable housing initiatives and increase funding for homeless services such as shelters, mental health treatment, and job training. Develop a comprehensive homelessness prevention and intervention strategy that addresses the root causes of homelessness such as poverty, mental illness, and addiction. Work with community organizations and advocates to identify and address local needs and priorities.",

    "Problem 9: Emergency services response time": "Implement a tiered emergency response system that prioritizes the most urgent calls and optimizes resources for maximum effectiveness. Encourage residents to use the MyLA311 app or hotline for non-emergency issues to free up emergency services for urgent situations. Increase public awareness of emergency response procedures and how to use 911 effectively.",

    "Problem 10: Lack of affordable housing": "Develop and implement affordable housing policies such as inclusionary zoning and rent control to ensure that all residents have access to safe, affordable housing. Encourage developers to include affordable units in new construction projects and provide incentives for landlords to maintain affordable rental rates. Work with community organizations and advocates to identify and address local needs and priorities."
}


# Create a list of clickable question titles
question_titles = [q for q in questions.keys()]


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
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text


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
    output = chatgpt_answer(user_input)
    # output = "hahaha"
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