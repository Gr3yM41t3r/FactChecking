from preTraitement import *
from similarityDetector import *

phrase1 = "Newt Gingrich says Freddie Mac, electric co-ops and credit unions are similar organizations"
phrase2 = "Gingrich repeats claim that Freddie Mac, credit unions are ‘government-sponsored enterprises’"
print("amine")
#pretrr1 = n_gram_start(phrase1)
#pretrr2 = n_gram_start(phrase2)
#print(pretrr1)
print(removeStopWords("Newt Gingrich says Freddie Mac, electric co-ops and credit unions are similar organizations"))
removeStopWordsCSV("abc","abc")

#print("jaccard:{} Cosine {}".format(Jaccard_distance(pretrr1, pretrr2), cosine_similarity_ngrams(pretrr1, pretrr2)))

##sameLignComparaison("claims_prof.csv", "similarity.csv")
