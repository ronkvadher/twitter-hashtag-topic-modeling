# src/hashtag_extraction.py
import re

def extract_hashtags(text):
    if not isinstance(text, str):
        return []
    hashtags = re.findall(r"#\w+", text)
    return [tag.lower().replace("#", "") for tag in hashtags]
