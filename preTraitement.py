import csv
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords

header = ['IdA', 'TextBefore', 'TextAfter']
data = []


def removeStopWords():
    stop_words = set(stopwords.words('english'))
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


removeStopWords()
