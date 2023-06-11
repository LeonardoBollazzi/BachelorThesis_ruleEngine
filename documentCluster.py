import germanStopwords
from sklearn.exceptions import ConvergenceWarning
import warnings
import paragraphObject
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def perform_text_clustering(paragraphs, clusters, num_clusters):
    warnings.filterwarnings("ignore", category=FutureWarning)
    warnings.filterwarnings("ignore", category=ConvergenceWarning)

    # Extract the content from each Paragraph object
    texts = [paragraph.modContent for paragraph in paragraphs]

    # Convert the list of texts into a matrix of TF-IDF features
    vectorizer = TfidfVectorizer(stop_words=germanStopwords.german_stopwords)
    tfidf_matrix = vectorizer.fit_transform(texts)

    # Perform clustering using KMeans
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(tfidf_matrix)

    # Get the cluster labels
    labels = kmeans.labels_

    # Dictionary used to store paragraphs in correct order
    dict = []
    # Assign cluster labels to each Paragraph object
    for i, paragraph in enumerate(paragraphs):
        paraClusterN = labels[i]
        position = None
        for dictEntry in dict:
            if paraClusterN == dictEntry[1]:
                position = dictEntry[0]
                break

        if position == None:
            position = len(dict)
            dict.append([position, paraClusterN])

        for cluster in clusters:
            if cluster.clusterN == position:
                # Inherit from the cluster by changing the paragraph's class
                paragraph.set_parentClusterN(cluster.clusterN)
                cluster.paragraphs.append(paragraph)
                break

    '''
    # Create a dictionary to store the clusters
    clusters = {cluster.clusterN: cluster.paragraphs for cluster in clusters}
    '''
    '''
        # Assign cluster labels to each Paragraph object
        for i, paragraph in enumerate(paragraphs):
            paragraph.clu = labels[i]
        '''
    '''
    # Create a dictionary to store the clusters
    clusters = {}
    for i, paragraph in enumerate(paragraphs):
        cluster_label = paragraph.clu
        if cluster_label not in clusters:
            clusters[cluster_label] = []
        clusters[cluster_label].append(paragraph)
    '''
    '''
    for c in clusters:
        print(c.clusterN)
        for p in c.paragraphs:
            print(p.clusterN)
            print(p.content)
            print("---------------")
    '''
    return clusters

def getTextCluster(paragraphs, clusters,k):
    num_clusters = k
    result = perform_text_clustering(paragraphs,clusters, num_clusters)
    return result