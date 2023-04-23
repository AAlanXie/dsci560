import streamlit as st

# Set page title and favicon
st.set_page_config(page_title="Project Models", page_icon=":bar_chart:")

# Define model information
models = [
    {
        "name": "VADER",
        "usage": "Sentiment Analysis",
        "description": "📈 VADER (Valence Aware Dictionary for Sentiment Reasoning) is a lexicon and rule-based sentiment analysis tool that addresses the limitations of traditional sentiment analysis tools when dealing with social media texts, which often contain non-standard language features such as slang and acronyms. It includes:\n\n* A lexicon of over 7,500 lexical features annotated with their sentiment polarity and intensity\n* A set of rules that take into account contextual information, such as punctuation and negations\n\nVADER has been shown to perform well in social media contexts and is widely used in sentiment analysis applications."
    },
    {
        "name": "YAKE",
        "usage": "Keyword Extraction",
        "description": "🔍 Yet Another Keyword Extractor (Yake) is a keyword extraction library that selects the most important keywords from a given text using the text statistical features method from the article. YAKE takes into account:\n\n* Word frequency, position, and co-occurrence to identify the most relevant keywords\n\nIt is a versatile library that can be used in a variety of applications, including:\n\n* Search engine optimization\n* Topic modeling\n* Document clustering"
    },
    {
        "name": "Transformers BART Model",
        "usage": "Text Summarization",
        "description": "📝 The Transformers BART (Bidirectional and Auto-Regressive Transformer) Model is a state-of-the-art text summarization model that aims to understand the entire document and generate paraphrased text to summarize the main points. BART uses a standard Seq2Seq bidirectional encoder (like BERT) and a left-to-right autoregressive decoder (like GPT) to combine the best of both worlds. It has been shown to achieve high accuracy and fluency in summarizing a variety of texts, including news articles, scientific papers, and legal documents. BART is a powerful tool for information retrieval and can save time and effort by quickly summarizing long texts. Some of its features include:\n\n* A bidirectional encoder that reads the entire document\n* A left-to-right autoregressive decoder that generates the summary\n* Paraphrasing capabilities that allow it to rephrase the text"
    }
]

# Display model information
for model in models:
    st.write(f"## {model['name']}")
    st.write(f"### {model['usage']}")
    st.write(model['description'])
    st.write("")
