import streamlit as st

# Set page title
st.set_page_config(page_title="Sentiment Analysis of City Services",
                   page_icon=":guardsman:", layout="wide")

# Add a title and subtitle with emojis
st.title("Sentiment Analysis of City Services 🏢🏬")
st.markdown(
    "Gain insights into public sentiment towards city services in Los Angeles and Pasadena areas.")

# Add an introduction section with team information
st.header("Introduction 🙌")
st.markdown("""
    Welcome to our website, NO LATE! We are a team of four students from USC. Our team members are:

    - Tianqi Xie
    - Li An
    - Bokai Yang
    - York Yao

    Our goal is to analyze public sentiment towards city services in the Los Angeles and Pasadena areas using data from social media platforms like Twitter and Reddit. By using sentiment analysis, we can identify potential problems with city services based on public views expressed on social media.

    The results of the sentiment analysis are displayed on [Analysis and Report](./page2) and [Latent Problems and Solution](./page3). Users can interact with ChatGPT on those pages to get basic solutions to the problems identified. 

    We hope that our website will provide useful insights for city officials and help improve city services based on public feedback. 🤞
""")

# Add a project workflow section with emojis
st.header("Project Workflow 🚀")
st.markdown("""
    Our project workflow consists of the following steps:

    1. **Social Media Data** 📊: Collect data from social media platforms like Twitter and Reddit.

    2. **Data Cleaning** 🧹: Preprocess the data to remove noise and irrelevant information.

    3. **Sentiment Analysis / Keyword Extraction / Summarization** 💬: Apply natural language processing techniques to analyze the data and extract sentiment, keywords, and summaries.

    4. **Sentiment Analysis -- Draw the Line Chart >> Show the Trends** 📈: Visualize the sentiment trends over time using a line chart.

    5. **Keyword Extraction -- Identify Latent Problems** 🔍: Identify potential problems with city services based on the keywords extracted from the data.

    6. **Latent Problems -- ChatGpt** 💡: Allow users to interact with ChatGPT to get basic solutions to the problems identified.
""")

# Add a footer with team information
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        font-size: 16px;
        color: white;
        background-color: #333333;
        padding: 10px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div class="footer">
        Made by NO LATE (Tianqi Xie, Li An, Bokai Yang, York Yao) 🤝
    </div>
    """,
    unsafe_allow_html=True
)
