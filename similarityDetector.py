import csv

from Levenshtein import distance
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model_name = 'bert-base-nli-mean-tokens'
model = SentenceTransformer(model_name)

header = ['IdA', 'IdB', 'TextA', 'TextB', 'LenA', 'LenB', 'Levenshtein-Distance', 'Jaccard_Distance',
          'Sentence_similarity_vect', 'similarity']
data = []


def longLineComparaison(inputfile, outputfile):
    counter = 0
    with open("claimskg_result.csv") as f:
        reader = csv.reader(f)
        myData = list(reader)
        with open('similarity.csv', 'w') as g:
            writer = csv.writer(g)
            writer.writerow(header)
            for row in myData:
                print(counter)
                counter = counter + 1
                for row2 in myData:
                    data.clear()
                    data.append(row[0])
                    data.append(row2[0])
                    data.append(row[1])
                    data.append(row2[1])
                    data.append(len(row[1]))
                    data.append(len(row2[1]))
                    distanced = distance(row[1], row2[1])
                    data.append(distanced)
                    data.append(Jaccard_Similarity(row[1], row2[1]))
                    data.append(sentence_Similarity(row[1], row2[1]))
                    if len(row2[1]) == 0:
                        quotiant = 0
                    else:
                        quotiant = (1 - (distanced / max(len(row[1]), len(row2[1])))) * 100
                    if quotiant > 50:
                        data.append(quotiant)
                        writer.writerow(data)


def sameLignComparaison(inputfile, outputfile):
    counter = 0
    with open(inputfile) as f:
        reader = csv.reader(f)
        myData = list(reader)
        with open(outputfile, 'w') as g:
            writer = csv.writer(g)
            writer.writerow(header)
            for row in myData:
                print(counter)
                counter = counter + 1
                data.clear()
                data.append(row[4])
                data.append(row[5])
                data.append(row[6])
                data.append(row[7])
                data.append(len(row[6]))
                data.append(len(row[7]))
                distanced = distance(row[6], row[7])
                data.append(distanced)
                jaccard = Jaccard_Similarity(row[6], row[7])
                data.append(jaccard)
                data.append(sentence_Similarity(row[6], row[7]))
                if len(row[7]) == 0:
                    quotiant = 0
                else:
                    quotiant = (1 - (distanced / max(len(row[6]), len(row[7])))) * 100
                data.append(quotiant)
                writer.writerow(data)


def sentence_Similarity(sentence1, sentence2):
    sentences_array = [sentence1, sentence2]
    sentence_vecs = model.encode(sentences_array)
    cosine_sim = cosine_similarity([sentence_vecs[0]], sentence_vecs[1:])
    return cosine_sim[0][0]


def Jaccard_Similarity(text1, text2):
    words_text1 = set(text1.lower().split())
    words_text2 = set(text2.lower().split())
    intersection = words_text1.intersection(words_text2)
    union = words_text1.union(words_text2)
    if len(union) == 0:
        return 0
    return float(len(intersection)) / len(union)

##sameLignComparaison("claims_prof.csv", "similarity.csv")
