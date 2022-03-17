import numpy as np
from sklearn.feature_extraction.text import  TfidfVectorizer
import pandas as pd
from IPython.display import display


docs = []

texte = ["This is an example of TfidfVectorizer for creating a vector",
 "This is another example of TfidfVectorizer",
 "with or without parameters"]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texte)
print(X)
df = pd.DataFrame(
 vectorizer.transform(texte).toarray(),
 vectorizer.get_feature_names()
)
display(df)



def tfidf(mot,text):
    tf = text.count(mot) /len(text)
    idf = np.log10(1/sum([1 for doc in docs if mot in doc]))
    return round(tf*idf, 4)
