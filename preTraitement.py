import csv
import re

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams

##nltk.download('wordnet')
##nltk.download('stopwords')
header = ['IdA', 'TextBefore', 'TextAfter']
data = []
# lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))


##----------------- stop words------------------------------
def removeStopWordsCSV(inputFile, outputFile):
    with open("inputCSV/small_claimskg_result.csv") as inputData:
        reader = csv.reader(inputData)
        claims = list(reader)
        with open("outputCSV/pretraiteCSV.csv", "w") as outputData:
            writer = csv.writer(outputData)
            writer.writerow(header)
            counter = 0
            for claim in claims:
                print(counter)
                counter = counter + 1
                data.clear()
                data.append(claim[0])
                data.append(claim[1])
                words = claim[1].split()
                textAfter = ""
                for r in words:
                    if not r in stop_words:
                        textAfter = textAfter + r + " "
                data.append(textAfter)
                writer.writerow(data)


def removeStopWords(text):
    words = text.split()
    pretrained_Text = ""
    for r in words:
        if not r in stop_words:
            pretrained_Text += r + " "
    return pretrained_Text


##------------------lemmatisation----------------------

def lemmatizer():
    print("rocks :", lemmatizer.lemmatize("rocks"))
    print("corpora :", lemmatizer.lemmatize("corpora"))


##-------------------------------NGram  tools--------------

NGRAM = 4
re_sent_ends_naive = re.compile(r'[.\n]')
re_stripper_alpha = re.compile(r'[^a-zA-Z]+')


def n_gram_start(text):
    if not text: return None
    ng = ngrams(re_stripper_alpha.sub(' ', text).split(), NGRAM)
    return list(ng)


paragraph = """It was the best of times, it was the worst of times.
               It was the age of wisdom? It was the age of foolishness!
               I first met Dr. Frankenstein in Munich; his monster was, presumably, at home."""

# a = n_gram_start(paragraph)
# print(len(a))
