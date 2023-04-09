# Contents of ~/my_app/main_page.py
import streamlit as st


def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")


st.markdown(
    '''
    # Solution of public’s livelihood problems based on Textual Analysis
    ### Team: No Late
    ##### Team Members: Bokai Yang, Li An, Tianqi Xie, York
    ''')

st.markdown('---')


st.markdown('''
    ## Project Description:
    This project aims to use Natural Language Processing (NLP) techniques to 
    process and analyze social media data from sources such as Twitter, 
    Reddit, and government websites within the Los Angeles area to understand the public's perception 
    and sentiment towards key city services such as transportation, waste management, 
    and public safety. The goal is to provide city officials with a comprehensive understanding 
    of the public's views on these services and inform decision-making efforts to enhance them, 
    resulting in increased customer satisfaction, reduced costs, and improved reputation for the city.
''')


space(2)

st.markdown('---')

st.markdown('''
    ## Project Workflow
    - Social Media Data 
    - Data cleaning
    - Sentiment Analysis / Keyword Extraction / Summarization
    - Sentiment -- Draw the line chart >> Show the trends
    - Keyword Extraction -- latent problems
    - latent problems -- ChatGpt
''')
