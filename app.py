# app.py
import streamlit as st
import pandas as pd

# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Twitter Hashtag Topic Modeling",
    layout="wide"
)

# --------------------------------------------------
# Load data once
# --------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/cleaned_tweets.csv")

df = load_data()

# --------------------------------------------------
# Header
# --------------------------------------------------
st.title("Twitter Hashtag Topic Modeling")

st.markdown(
    """
    This application presents the results of an NLP-based system that identifies
    trending topics from Twitter hashtags using **Latent Dirichlet Allocation (LDA)**
    and **automatic topic labeling with Large Language Models (LLMs)**.
    """
)

st.markdown("---")

# --------------------------------------------------
# Trending hashtags
# --------------------------------------------------
st.subheader("Trending Hashtags")

st.markdown(
    "The following visualization shows the most frequently occurring hashtags "
    "after preprocessing, indicating dominant trends in the dataset."
)

st.image(
    "outputs/plots/top_hashtags.png",
    use_column_width=True
)

st.markdown("---")

# --------------------------------------------------
# Topic modeling results
# --------------------------------------------------
st.subheader("Topic Modeling Results")

st.markdown(
    "Topics are first discovered using LDA and then automatically labeled "
    "to improve interpretability."
)

col1, col2 = st.columns(2)

with col1:
    st.markdown("**LDA Topic Keywords**")
    with open("outputs/topics.txt", "r") as f:
        st.text(f.read())

with col2:
    st.markdown("**Automatically Generated Topic Labels**")
    with open("outputs/topic_labels.txt", "r") as f:
        st.text(f.read())

st.markdown("---")

# --------------------------------------------------
# Dataset preview
# --------------------------------------------------
st.subheader("Cleaned Hashtag Text (Sample)")

st.markdown(
    "Below is a small sample of the cleaned hashtag text used for topic modeling."
)

st.dataframe(
    df[["clean_text"]].head(30),
    use_container_width=True
)

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.markdown(
    "Developed by **Ronak Vadher**  \n"
    "NLP Project — Twitter Hashtag Topic Modeling"
)

