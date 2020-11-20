"""
This script contains the code to train lda

EMSE_DevInt>python ./python/train_lda.py 5 10 D:\Victoria\EMSE\p2\EMSE_DevInt\python\data\data_processed\processed_data.csv
"""

import pandas as pd
from sklearn.decomposition import LatentDirichletAllocation as LDA
from sklearn.feature_extraction.text import CountVectorizer
import sys

# read data from the file and return the whole csv and the series of procesed data
def read_data(filepath):
    data = pd.read_csv(filepath)
    processed_data = data['processed_title_and_text']
    return data, processed_data


# create a count vectorizer
def create_count_vectorizer(processed_data):
    # Create a count vectorizer
    count_vectorizer = CountVectorizer()
    # Fit and transform the processed titles
    count_data = count_vectorizer.fit_transform(processed_data)

    return count_vectorizer, count_data

# Print the topics found by the LDA model
def print_topics(model, count_vectorizer, n_top_words, _print):
    words = count_vectorizer.get_feature_names()
    topics = []
    for topic_idx, topic in enumerate(model.components_):
        if _print:
            print("\nTopic #%d:" % topic_idx)
            print(" ".join([words[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]]))
        topics.append([words[i]
                        for i in topic.argsort()[:-n_top_words - 1:-1]])
    return topics


# Create and fit the LDA model
def create_topics(processed_data, number_topics=5, number_words=10, _print=True):
    # Create a count vectorizer
    count_vectorizer, count_data = create_count_vectorizer(processed_data)

    lda = LDA(n_components=number_topics, n_jobs=-1)
    lda.fit(count_data)

    topics = print_topics(lda, count_vectorizer, number_words, _print)

    return lda, topics, count_vectorizer

def main(argv):
    number_topics = int(argv[1])
    number_words = int(argv[2])
    datafilepath = argv[3]
    data, processed_data = read_data(datafilepath)
    _, _, _ = create_topics(processed_data, number_topics=number_topics, number_words=number_words)



if __name__ == '__main__':
    main(sys.argv)