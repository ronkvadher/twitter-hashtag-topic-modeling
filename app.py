# app.py
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Twitter Hashtag Topic Modeling", layout="wide")

st.title("Twitter Hashtag Topic Modeling")
st.write(
    "This application identifies trending hashtags from Twitter data "
    "and automatically discovers underlying topics using NLP and topic modeling."
)

# Load cleaned data
df = pd.read_csv("data/cleaned_tweets.csv")

st.subheader("Sample Cleaned Hashtags")
st.dataframe(df[["clean_text"]].head(20))

# Show trending hashtags plot
st.subheader("Top Trending Hashtags")
st.image("outputs/plots/top_hashtags.png")

# Show raw LDA topics
st.subheader("Discovered Topics (LDA Keywords)")
with open("outputs/topics.txt", "r") as f:
    st.text(f.read())

# Show automatically labeled topics
st.subheader("Automatically Labeled Topics")
with open("outputs/topic_labels.txt", "r") as f:
    st.text(f.read())