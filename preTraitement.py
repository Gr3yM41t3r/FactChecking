import re

import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.util import ngrams  # This is the ngram magic
from sklearn.feature_extraction.text import TfidfVectorizer

from fmeasures import fMeasure
from similarityDetector import *

# lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
tfidf_vectorizer = TfidfVectorizer()
tokenizer = RegexpTokenizer(r'\w+')
re_stripper_alpha = re.compile('[^a-zA-Z]+')

header = ['IdA', 'TextBefore', 'TextAfter']
data = []


##----------------- stop words------------------------------

def removeStopWords(text):
    words = text.split()
    pretrained_Text = ""
    for r in words:
        if not r in stop_words:
            pretrained_Text += r + " "
    return pretrained_Text


##-------------------------------NGram  tools--------------


def nGRAM(txt, NGRAM):
    """Get tuples that ignores all punctuation (including sentences)."""
    if not txt: return None
    ng = ngrams(re_stripper_alpha.sub(' ', txt).split(), NGRAM)
    return list(ng)


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


def nGram_similarity(s1, s2, n):
    return len(intersection(nGRAM(s1, n), nGRAM(s2, n))) / (min(len(s1.split()), len(s2.split())) - n + 1)


def getResult(id, textScore, keywordsScore):
    if textScore > 0.6:
        print("{}--->E".format(id))
        return "E"
    elif 0.35 < textScore <= 0.6:
        if 0.3 < keywordsScore < 0.8:
            print("{}--->ST".format(id))
            return 'ST'
    elif textScore <= 0.35:
        print("{}--->N".format(id))
        return 'N'
    else:
        print("waaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaA3", id)


def makeResulat(textscor, threshold):
    if textscor < threshold:
        return 'E'


def removeStopWordsProfCsv(threshold):
    header2 = ['TexteA', 'TextB', 'TextAPT', 'TextBPT', 'TFIDF', 'Jaccard_Distance', 'Levenshtein_Distance',
               'NGram-Similarity', 'EXPECTED',
               'RESULT', 'Score Keywords']
    corpus = []
    corpuskeywords = []
    with open('outputCSV/claims_benc.csv') as inputData:
        reader = csv.reader(inputData)
        claims = list(reader)
        with open("outputCSV/pretraiteCSV.csv", "w") as outputData:
            writer = csv.writer(outputData)
            writer.writerow(header2)
            counter = 1
            for claim in claims:
                # print(counter)
                counter += 1
                # data reset
                data.clear()
                corpus.clear()
                corpuskeywords.clear()
                # original text A and B before Modifications
                textA = claim[6]
                textB = claim[7]
                # text A and B after removing stop words lowering and removine punctuation
                textA_After = removeStopWords(' '.join(tokenizer.tokenize(textA.lower())))
                textB_After = removeStopWords(' '.join(tokenizer.tokenize(textB.lower())))

                # keyword 
                keywordsA = removeStopWords(' '.join(tokenizer.tokenize(claim[10].lower())))
                keywordsB = removeStopWords(' '.join(tokenizer.tokenize(claim[11].lower())))
                # print('{} : {}'.format(counter, claim[10]))
                # calculating TF-IDF TEXTE
                corpus.append(textA_After)
                corpus.append(textB_After)
                tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)
                cosine = cosine_similarity(tfidf_matrix, tfidf_matrix)
                tfidf_value = round(cosine[0][1], 2)

                # calculating TF-IDF kEYWORDS                
                corpuskeywords.append(keywordsA)
                corpuskeywords.append(keywordsB)
                tfidf_matrix = tfidf_vectorizer.fit_transform(corpuskeywords)
                cosine = cosine_similarity(tfidf_matrix, tfidf_matrix)
                tfidf_key_value = cosine[0][1]
                # calculation Jaccard_Distance
                jaccard_distance = Jaccard_distance(textA_After, textB_After)
                # calculation Levenshtein_Distance
                lev_distance = Levenshtein_Distance(textA_After, textB_After)
                # calculation Ngram_similarity
                ngram_similarity = nGram_similarity(textA, textB, 3)
                # Expected Result for similarity
                expected_Similarity = claim[0]
                # Actual  model similarity
                # print("id: {}  TFIDF: {} TFIDF2: {}".format(counter,tfidf_value,tfidf_key_value))
                # actual_result = getResult(counter, tfidf_value, tfidf_key_value)
                actual_result = makeResulat(tfidf_key_value, threshold)
                # adding data
                data.append(textA)
                data.append(textB)
                data.append(textA_After)
                data.append(textB_After)
                data.append(tfidf_value)
                data.append(jaccard_distance)
                data.append(lev_distance)
                data.append(ngram_similarity)
                data.append(expected_Similarity)
                data.append(actual_result)
                data.append(tfidf_key_value)
                writer.writerow(data)


# removeStopWordsProfCsv()
def start():
    header = ['threshold', 'fmeasure']
    date =[]
    with open('classeDetector/EFIDF_KEYWORDS.csv', 'w+') as output:
        writer = csv.writer(output)
        writer.writerow(header)
        for i in np.arange(0, 1.02, 0.05):
            print(i)
            date.clear()
            removeStopWordsProfCsv(i)
            score = fMeasure("E")
            date.append(i)
            date.append(score)
            writer.writerow(date)

start()
'''
classes = ["E", "ST", "N"]
total = 0
for i in classes:
    score = fMeasure(i)
    print("{}: {}".format(i, score))
    total += score
print("total: ", total / len(classes))
'''
