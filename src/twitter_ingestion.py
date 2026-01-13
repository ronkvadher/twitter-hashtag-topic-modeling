# src/twitter_ingestion.py
import tweepy
import os
import pandas as pd

def fetch_tweets(query, max_results=100):
    bearer_token = os.getenv("TWITTER_BEARER_TOKEN")
    if not bearer_token:
        raise RuntimeError("TWITTER_BEARER_TOKEN not set")

    client = tweepy.Client(bearer_token=bearer_token)

    tweets = client.search_recent_tweets(
        query=query,
        max_results=max_results,
        tweet_fields=["created_at", "lang"]
    )

    data = []
    if tweets.data:
        for tweet in tweets.data:
            data.append({
                "content": tweet.text,
                "date_time": tweet.created_at,
                "language": tweet.lang
            })

    return pd.DataFrame(data)
