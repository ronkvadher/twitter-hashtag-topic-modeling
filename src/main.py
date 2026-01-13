import pandas as pd
from hashtag_extraction import extract_hashtags
from data_preprocessing import preprocess_text
from topic_modeling import run_lda
from visualization import plot_top_hashtags
from smart_topic_labeling import auto_label_topic
from twitter_ingestion import fetch_tweets

# CONFIGURATION FLAG
# False = use dataset (default, deployment-safe)
# True  = fetch live tweets via Twitter (X) API
USE_TWITTER_API = False

def main():
    # DATA INGESTION

    if USE_TWITTER_API:
        print("Fetching tweets via Twitter API...")
        df = fetch_tweets(
            query="#worldcup OR #music OR #election",
            max_results=200
        )
        df.to_csv("../data/tweets.csv", index=False)
        print("Tweets fetched and saved.")
    else:
        print("Loading dataset...")
        df = pd.read_csv("../data/tweets.csv")


    # BASIC FILTERING
    df = df[["content", "date_time", "language"]]
    df = df[df["language"] == "en"]


    # HASHTAG EXTRACTION
    print("Extracting hashtags...")
    df["hashtags"] = df["content"].apply(extract_hashtags)
    df = df[df["hashtags"].apply(len) > 0]


    # TEXT PREPROCESSING
    print("Preprocessing text...")
    df["hashtag_text"] = df["hashtags"].apply(lambda x: " ".join(x))
    df["clean_text"] = df["hashtag_text"].apply(preprocess_text)
    df = df[df["clean_text"].str.split().apply(len) >= 2]

    df.to_csv("../data/cleaned_tweets.csv", index=False)
    print("Cleaned data saved.")


    # TOPIC MODELING
    print("Running LDA topic modeling...")
    topics = run_lda(df["clean_text"])


    # AUTOMATIC TOPIC LABELING (LLM-BASED)
    print("Automatically labeling topics (LLM-based)...")

    with open("../outputs/topic_labels.txt", "w") as f:
        for i, topic in enumerate(topics):
            label = auto_label_topic(topic)
            f.write(f"Topic {i + 1}: {label}\n")

    print("Topics saved.")


    # VISUALIZATION
    print("Generating visualizations...")
    plot_top_hashtags(df)

    print("Pipeline execution completed successfully.")


if __name__ == "__main__":
    main()