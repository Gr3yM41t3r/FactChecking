from preTraitement import removeStopWordsCSV, removeStopWords
from similarityDetector import *

from sklearn.metrics.pairwise import  cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer



phrase1 = "Newt Gingrich says Freddie Mac, electric co-ops and credit unions are similar organizations"
phrase2 = "Gingrich repeats claim that Freddie Mac, credit unions are ‘government-sponsored enterprises’"
print("amine")
#pretrr1 = n_gram_start(phrase1)
#pretrr2 = n_gram_start(phrase2)
#print(pretrr1)
#print(removeStopWords("Newt Gingrich says Freddie Mac, electric co-ops and credit unions are similar organizations"))
#removeStopWordsCSV("abc","abc")

corpus = ['Cory Booker claims Devils managing partner Jeff Vanderbeek refused to give any of the charitable dollars required under lease agreement for the Prudential Center',
          'Cory Booker claims Jeff Vanderbeek “took us into arbitration” in dispute over Prudential Center',
    ]



# Initialize an instance of tf-idf Vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Generate the tf-idf vectors for the corpus
tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)

# compute and print the cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
print(cosine_sim)

#print("jaccard:{} Cosine {}".format(Jaccard_distance(pretrr1, pretrr2), cosine_similarity_ngrams(pretrr1, pretrr2)))

##sameLignComparaison("claims_prof.csv", "similarity.csv")
