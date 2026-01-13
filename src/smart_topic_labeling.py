import os
import subprocess

# Try OpenAI (ChatGPT API)
from openai import OpenAI

def label_with_openai(topic_words):
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not set")

        client = OpenAI(api_key=api_key)

        prompt = f"""
        You are an NLP system.
        Given the following topic keywords extracted from Twitter hashtags:

        {', '.join(topic_words)}

        Return ONLY a short topic label (2–5 words).
        Do NOT explain.
        Do NOT add punctuation.
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        return response.choices[0].message.content.strip()

    except Exception:
        return None

# Try Ollama (Local LLM)
def label_with_ollama(topic_words):
    try:
        prompt = f"""
        Label the following topic keywords with a short topic name.
        Return ONLY the label.

        {', '.join(topic_words)}
        """

        result = subprocess.run(
            ["ollama", "run", "mistral"],
            input=prompt,
            text=True,
            capture_output=True,
            timeout=30
        )

        if result.returncode != 0:
            return None

        return result.stdout.strip()

    except Exception:
        return None

# Smart Auto Label Function
def auto_label_topic(topic_words):
    """
    Automatically labels a topic using:
    1. ChatGPT API (if available)
    2. Ollama (if available)
    3. Raises error if neither works
    """

    label = label_with_openai(topic_words)
    if label:
        return label

    label = label_with_ollama(topic_words)
    if label:
        return label

    raise RuntimeError(
        "Automatic topic labeling failed: "
        "No valid OpenAI API key and Ollama is not available."
    )
