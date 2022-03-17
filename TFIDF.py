import numpy as np

docs = []
def tfidf(mot,text):
    tf = text.count(mot) /len(text)
    idf = np.log10(1/sum([1 for doc in docs if mot in doc]))
    return round(tf*idf, 4)
