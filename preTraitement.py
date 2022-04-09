import re

from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.util import ngrams  # This is the ngram magic
from sklearn.feature_extraction.text import TfidfVectorizer

from similarityDetector import *

##nltk.download('wordnet')
##nltk.download('stopwords')

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
    if not txt : return None
    ng = ngrams(re_stripper_alpha.sub(' ', txt).split(), NGRAM)
    return list(ng)

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def nGram_similarity(s1, s2, n):
    return len(intersection(nGRAM(s1, n), nGRAM(s2, n))) / (min(len(s1.split()), len(s2.split())) - n + 1)


def getResult(TFIDF, Jac):
    if TFIDF > 0.98 and Jac > 0.98:
        return "E"
    elif TFIDF > 0.5 and Jac < 0.5:
        return 'N'
    elif TFIDF < 0.5 and Jac > 0.5:
        return 'ST'
    elif 0.5 < TFIDF < 0.9 and 0.5 < Jac < 0.9:
        return "E*"
    elif 0.3 < TFIDF < 0.5 and 0.3 < Jac < 0.5:
        return "ST"
    elif TFIDF < 0.3 and Jac < 0.3:
        return 'N'


def countRightAnswers():
    with open("outputCSV/pretraiteCSV.csv") as input:
        reader = csv.reader(input)
        results = list(reader)
        right_answers = 0
        for result in results:
            if result[8] == result[9]:
                right_answers += 1
        print((right_answers / len(results)) * 100)


def removeStopWordsProfCsv():
    header2 = ['TexteA', 'TextB', 'TextAPT', 'TextBPT', 'TFIDF', 'Jaccard_Distance', 'Levenshtein_Distance',
               'NGram-Similarity', 'EXPECTED',
               'RESULT']
    corpus = []
    with open('inputCSV/claims_prof.csv') as inputData:
        reader = csv.reader(inputData)
        claims = list(reader)
        with open("outputCSV/pretraiteCSV.csv", "w") as outputData:
            writer = csv.writer(outputData)
            writer.writerow(header2)
            counter = 0
            for claim in claims:
                print(counter)
                counter += 1
                # data reset
                data.clear()
                corpus.clear()
                # original text A and B before Modifications
                textA = claim[6]
                textB = claim[7]
                # text A and B after removing stop words lowering and removine punctuation
                textA_After = removeStopWords(' '.join(tokenizer.tokenize(textA.lower())))
                textB_After = removeStopWords(' '.join(tokenizer.tokenize(textB.lower())))
                # calculating TF-IDF
                corpus.append(textA_After)
                corpus.append(textB_After)
                tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)
                cosine = cosine_similarity(tfidf_matrix, tfidf_matrix)
                tfidf_value = cosine[0][1]
                # calculation Jaccard_Distance
                jaccard_distance = Jaccard_distance(textA_After, textB_After)
                # calculation Levenshtein_Distance
                lev_distance = Levenshtein_Distance(textA_After, textB_After)
                # calculation Ngram_similarity
                ngram_similarity = nGram_similarity(textA, textB, 3)
                # Expected Result for similarity
                expected_Similarity = claim[0]
                # Actual  model similarity
                actual_result = getResult(tfidf_value, jaccard_distance)
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

                writer.writerow(data)


removeStopWordsProfCsv()
countRightAnswers()


##------------------lemmatisation----------------------

def lemmatizer():
    print("rocks :", lemmatizer.lemmatize("rocks"))
    print("corpora :", lemmatizer.lemmatize("corpora"))
