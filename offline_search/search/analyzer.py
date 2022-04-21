import re
import string
# from Stemmer import Stemmer
from nltk import SnowballStemmer


# English language most common words:
# English language most common words:
Stopwords = set(["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves",
                 "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their",
                 "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was",
                 "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and",
                 "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against",
                 "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down",
                 "in", "out", "over", "under", "again", "further", "then", "once", "here", "there", "when",
                 "where", "why", "how", "How", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no",
                 "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now",
                 "accordance", "according", "accordingly", "across", "act", "actually", "on", "non", "of", "onn", "off"])
Puntuation = re.compile('[%s]' % re.escape(string.punctuation))
# STEMMER = Stemmer.Stemmer('english')
Snowball = SnowballStemmer('english')

#Pre-processing raw text

def tokenize(text):
    return text.split()

def lowercase_filter(tokens):
    return [token.lower() for token in tokens]

def punctuation_filter(tokens):
    return [Puntuation.sub('', token) for token in tokens]

def stopword_filter(tokens):
    return [token for token in tokens if token not in Stopwords]

def stem_filter(tokens):
    return [Snowball.stem(token) for token in tokens]

def analyze(text):
    tokens = tokenize(text)
    tokens = lowercase_filter(tokens)
    tokens = punctuation_filter(tokens)
    tokens = stopword_filter(tokens)
    tokens = stem_filter(tokens)
    token = [token for token in tokens if token]
    return token
