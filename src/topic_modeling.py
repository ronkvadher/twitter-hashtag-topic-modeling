# src/topic_modeling.py
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def run_lda(texts, n_topics=5, n_words=10):
    vectorizer = CountVectorizer(max_df=0.85, min_df=15, stop_words="english")
    X = vectorizer.fit_transform(texts)

    lda = LatentDirichletAllocation(
        n_components=n_topics,
        random_state=42
    )
    lda.fit(X)

    feature_names = vectorizer.get_feature_names_out()

    topics = []
    for idx, topic in enumerate(lda.components_):
        words = [feature_names[i] for i in topic.argsort()[-n_words:]]
        topics.append(words)

    return topics