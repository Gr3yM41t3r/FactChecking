import csv

from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.util import ngrams # This is the ngram magic.
import re



tokenizer = RegexpTokenizer(r'\w+')
abc = ' '.join(tokenizer.tokenize('Eighty-seven miles to go, yet.  Onward!'.lower()))
print(abc)

re_stripper_alpha = re.compile('[^a-zA-Z]+')



phrase1 = "Newt Gingrich says Freddie Mac, electric co-ops and credit unions are similar organizations"
phrase2 = "Gingrich repeats claim that Freddie Mac, credit unions are ‘government-sponsored enterprises’"


def ngrams(sentence, n):
  return zip(*[sentence.split()[i:] for i in range(n)])

print(set(ngrams(phrase2,3)))


def return_avg_value():
    with open("outputCSV/pretraiteCSV.csv") as inputData:
        reader = csv.reader(inputData)
        claims = list(reader)
        sum_of_value_jav = 0
        sum_of_value_tfidf = 0
        count = 0
        for claim in claims:
            if claim[7] == "N":
                sum_of_value_jav += float(claim[5])
                sum_of_value_tfidf += float(claim[4])
                count += 1
        print("TFIDF : " , (sum_of_value_tfidf/count)*100)
        print("jac : " , (sum_of_value_jav/count)*100)

#return_avg_value()