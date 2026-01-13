# app.py
import streamlit as st
import pandas as pd

# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Twitter Hashtag Topic Modeling",
    page_icon="📈",
    layout="wide"
)

# --------------------------------------------------
# Load data
# --------------------------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("data/cleaned_tweets.csv")

df = load_data()

# --------------------------------------------------
# Sidebar Navigation
# --------------------------------------------------
st.sidebar.title("Dashboard")
st.sidebar.markdown("NLP Project Navigation")

section = st.sidebar.radio(
    "Select Section",
    [
        "Overview",
        "Trending Hashtags",
        "Topic Modeling",
        "Dataset Preview"
    ]
)

# --------------------------------------------------
# OVERVIEW
# --------------------------------------------------
if section == "Overview":
    st.title("Twitter Hashtag Topic Modeling")

    st.markdown(
        """
        This project applies **Natural Language Processing (NLP)** techniques to analyze 
        Twitter hashtags and identify **trending discussion topics**.

        The system uses **Latent Dirichlet Allocation (LDA)** for topic discovery and 
        **Large Language Models (LLMs)** for automatic topic labeling, improving the 
        interpretability of unsupervised topics.
        """
    )

    st.markdown("### Key Features")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            - Hashtag extraction and preprocessing  
            - Unsupervised topic modeling (LDA)  
            - Automatic topic labeling (LLM-based)  
            """
        )

    with col2:
        st.markdown(
            """
            - Trend visualization  
            - Modular and extensible design  
            - Streamlit-based web interface  
            """
        )

# --------------------------------------------------
# TRENDING HASHTAGS
# --------------------------------------------------
elif section == "Trending Hashtags":
    st.title("Trending Hashtags")

    st.markdown(
        "The chart below shows the **top trending hashtags** based on frequency "
        "after preprocessing."
    )

    # Control image size using columns
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.image(
            "outputs/plots/top_hashtags.png",
            caption="Top Trending Hashtags",
            use_column_width=True
        )

# --------------------------------------------------
# TOPIC MODELING
# --------------------------------------------------
elif section == "Topic Modeling":
    st.title("Topic Modeling Results")

    st.markdown(
        "Topics are first discovered using **LDA** and then automatically labeled "
        "using **Large Language Models**."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("LDA Topic Keywords")
        st.markdown(
            "These represent the most important keywords for each topic discovered "
            "by the LDA model."
        )
        with open("outputs/topics.txt", "r") as f:
            st.text(f.read())

    with col2:
        st.subheader("Automatically Labeled Topics")
        st.markdown(
            "These concise labels are generated automatically to improve topic "
            "interpretability."
        )
        with open("outputs/topic_labels.txt", "r") as f:
            st.text(f.read())

# --------------------------------------------------
# DATASET PREVIEW
# --------------------------------------------------
elif section == "Dataset Preview":
    st.title("Cleaned Hashtag Dataset")

    st.markdown(
        "Below is a preview of the **cleaned hashtag text** used as input for topic modeling."
    )

    st.dataframe(
        df[["clean_text"]].head(40),
        use_container_width=True
    )

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.markdown(
    "Developed by **Ronak Vadher and Tanishq Bhalekar**  \n"
    "NLP Project | Twitter Hashtag Topic Modeling"
)
