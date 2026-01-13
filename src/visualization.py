# src/visualization.py
import matplotlib.pyplot as plt
from collections import Counter

def plot_top_hashtags(df):
    hashtags = [tag for tags in df["hashtags"] for tag in tags]
    counter = Counter(hashtags).most_common(10)

    words, counts = zip(*counter)

    plt.figure(figsize=(8, 5))
    plt.bar(words, counts)
    plt.xticks(rotation=45)
    plt.title("Top 10 Trending Hashtags")
    plt.tight_layout()
    plt.savefig("../outputs/plots/top_hashtags.png")
    plt.close()