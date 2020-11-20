import sklearn as sk
import numpy as np
import scipy
import nltk
from nltk.corpus import stopwords
import re
from nltk.stem import PorterStemmer

nltk.download('stopwords')

# replcae non alpha numeric charactor with space given a text
def remove_non_alphabetic_characters(text):
    text= re.sub('[^a-zA-Z]+', ' ', text)
    text = re.sub('[\s]+', ' ', text)
    return text

# tokenize from space given a text
def tockenize(text):
    tokens = text.split(" ")
    if "" in tokens:
        tokens.remove("")
    return tokens

# remove words that contain non alpha numeric characters given a list of tokens
# this not used for processing
def remove_non_alphabetic_tokens(tokens):
    tokens = [word for word in tokens if word.isalpha()]
    return tokens

# remove stop words such as to,... given a list of tokens
def remove_stop_words(tokens):
    stop_words = set(stopwords.words('english'))
    tokens = [w for w in tokens if not w in stop_words]
    return tokens

# stemming the words to original stem given a list of tokens
def stem(tokens):
    ps = PorterStemmer() 
    tokens = [ps.stem(w) for w in tokens]
    return tokens

# remove words less than a certain length givena list of tokens
def remove_short_tokens(tokens,length=1):
    tokens = [word for word in tokens if len(word) > length]
    return tokens

# combining the methods defined to process a given text and return the processed text
def process (title):
    title = title.lower()
    title = remove_non_alphabetic_characters(title)
    tokens = tockenize(title)
    tokens = remove_stop_words(tokens)
    tokens = stem(tokens)
    tokens = remove_short_tokens(tokens)
    processed_text = ' '.join(tokens)
    return processed_text
