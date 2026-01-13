# Twitter Hashtag Topic Modeling using NLP

## Project Overview
This project focuses on identifying **trending topics on Twitter (X)** by analyzing hashtags using **Natural Language Processing (NLP)** and **topic modeling techniques**.  
The system extracts hashtags from tweets, preprocesses them, discovers latent topics using **Latent Dirichlet Allocation (LDA)**, and finally assigns **human-readable topic labels automatically using Large Language Models (LLMs)**.

The project is designed as a **full end-to-end NLP application**, including:
- Data ingestion (dataset and API-ready architecture)
- Topic modeling
- Automatic topic labeling
- Visualization
- Web deployment using Streamlit

---

## Objectives
- Extract and preprocess hashtags from Twitter data
- Identify trending topics using unsupervised topic modeling
- Automatically label discovered topics using LLMs
- Visualize hashtag trends
- Deploy results via a web interface
- Design an extensible architecture that supports real-time Twitter API ingestion

---

## Project Architecture

Twitter Dataset / Twitter API (optional)
↓
Hashtag Extraction
↓
Text Preprocessing (NLP)
↓
LDA Topic Modeling
↓
LLM-based Automatic Topic Labeling
↓
Saved Outputs (CSV, TXT, PNG)
↓
Streamlit Web Application


---

## Dataset
- **Source**: Twitter dataset (CSV)
- **Key Columns**:
  - `content` – tweet text
  - `date_time` – tweet timestamp
  - `language` – tweet language
- Only **English tweets** are used for analysis.

The cleaned dataset is saved as:

data/cleaned_tweets.csv


---

## NLP Preprocessing
The following preprocessing steps are applied:
- Hashtag extraction from tweet text
- Lowercasing
- Removal of special characters and numbers
- Stopword removal (NLTK)
- Lemmatization
- Filtering out very short or noisy hashtag phrases

This ensures that only **meaningful hashtag text** is used for topic modeling.

---

## Topic Modeling (LDA)
- Algorithm: **Latent Dirichlet Allocation (LDA)**
- Library: `scikit-learn`
- Input: Cleaned hashtag text
- Output:
  - A fixed number of latent topics
  - Each topic represented by its top keywords

Topics are stored in:

outputs/topics.txt


---

## Automatic Topic Labeling (LLM-based)
To convert raw LDA keywords into **human-readable topic names**, the project uses **Large Language Models (LLMs)**.

### Supported Labeling Modes
1. **OpenAI API (ChatGPT)** – primary option  
2. **Ollama (local LLM)** – fallback option  
3. **Graceful error handling** if no LLM is available

The labeling process is:
- Fully automatic
- Performed **after LDA**
- Produces concise topic names (2–5 words)

Final labels are saved in:

---

## Automatic Topic Labeling (LLM-based)
To convert raw LDA keywords into **human-readable topic names**, the project uses **Large Language Models (LLMs)**.

### Supported Labeling Modes
1. **OpenAI API (ChatGPT)** – primary option  
2. **Ollama (local LLM)** – fallback option  
3. **Graceful error handling** if no LLM is available

The labeling process is:
- Fully automatic
- Performed **after LDA**
- Produces concise topic names (2–5 words)

Final labels are saved in:

outputs/topic_labels.txt


This makes the system significantly more interpretable than traditional topic modeling approaches.

---

## Twitter (X) API Integration (Architectural Support)
The project includes **built-in support for real-time Twitter API ingestion** using the official X (Twitter) API v2.

- API logic is isolated in:

src/twitter_ingestion.py

- Controlled via a feature flag:
```python
USE_TWITTER_API = False

Current Status

Due to recent API pricing changes, dataset-based ingestion is used for experimentation.
However, the architecture fully supports live data ingestion by simply:

Enabling the flag

Providing a valid Bearer Token

This ensures the project is future-ready and industry-aligned.

Visualization

The project generates a visualization showing:

Top 10 trending hashtags by frequency

## Output file:

outputs/plots/top_hashtags.png

## Web Application (Streamlit)

A Streamlit web application is used to present results interactively.

Features:

Displays sample cleaned hashtags

Shows trending hashtag visualization

Displays raw LDA topics

Displays automatically labeled topics

The app is read-only and does not perform heavy computation at runtime, making it deployment-safe.

Entry file:

app.py


## Deployment

The project is designed for deployment on Streamlit Cloud.

Deployment Characteristics:

Publicly accessible web interface

No API keys required at runtime

Uses precomputed outputs

Lightweight and reproducible

## Technologies Used

Programming Language: Python

NLP: NLTK

Topic Modeling: Scikit-learn (LDA)

LLMs: OpenAI API / Ollama (optional)

Visualization: Matplotlib

Web Framework: Streamlit

Version Control: Git & GitHub

## How to Run the Project (Local)

1. Install dependencies
pip install -r requirements.txt

2. Run the backend pipeline
cd src
python main.py

3. Launch the Streamlit app
streamlit run app.py

Author

Ronak Vadher