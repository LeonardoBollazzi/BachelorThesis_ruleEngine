from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.exceptions import ConvergenceWarning
import warnings

import germanStopwords


def find_optimal_clusters(paragraphs, max_clusters):
    warnings.filterwarnings("ignore", category=FutureWarning)
    warnings.filterwarnings("ignore", category=ConvergenceWarning)

    texts = [paragraph.modContent for paragraph in paragraphs]

    # Convert the list of texts into a matrix of TF-IDF features
    vectorizer = TfidfVectorizer(stop_words=germanStopwords.german_stopwords)
    tfidf_matrix = vectorizer.fit_transform(texts)

    silhouette_scores = []
    for num_clusters in range(2, max_clusters + 1):
        kmeans = KMeans(n_clusters=num_clusters, n_init='auto')
        kmeans.fit(tfidf_matrix)
        labels = kmeans.labels_
        silhouette_avg = silhouette_score(tfidf_matrix, labels)
        silhouette_scores.append(silhouette_avg)

    # Calculate the optimal value of k
    optimal_k = silhouette_scores.index(max(silhouette_scores)) + 2  # Adding 2 to account for starting from k=2

    return optimal_k

def get_Optimal_K(paragraphs):
    max_clusters = (len(paragraphs) - 1)
    optimalK = find_optimal_clusters(paragraphs, max_clusters)
    print("optimal: " + str(optimalK) + "\n")
    return optimalK