from Levenshtein import distance
import csv
import nltk

nltk.download('punkt')
from nltk import sent_tokenize

header = ['IdA', 'IdB', 'TextA', 'TextB', 'LenA', 'LenB', 'Levenshtein-Distance', 'Jaccard_Distance', 'similarity']
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
                ##print(counter)
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
                jaccard=Jaccard_Similarity(row[6], row[7])
                print(jaccard)
                data.append(jaccard)
                if len(row[7]) == 0:
                    quotiant = 0
                else:
                    quotiant = (1 - (distanced / max(len(row[6]), len(row[7])))) * 100
                data.append(quotiant)
                print(data)
                writer.writerow(data)


def Jaccard_Similarity(text1, text2):
    words_text1 = set(text1.lower().split())
    words_text2 = set(text2.lower().split())
    intersection = words_text1.intersection(words_text2)
    union = words_text1.union(words_text2)
    if len(union) == 0:
        return 0
    return float(len(intersection)) / len(union)

##sameLignComparaison("claims_prof.csv", "similarity.csv")
