from Levenshtein import distance
import csv

header = ['IdA', 'IdB', 'TextA', 'TextB', 'LenA', 'LenB', 'Levenshtein-Distance', 'similarity']
data = []
###
with open("small_claimskg_result.csv") as f:
    reader = csv.reader(f)
    myData = list(reader)
    with open('similarity.csv', 'w') as g:
        writer = csv.writer(g)
        writer.writerow(header)
        for row in myData:
            for row2 in myData:
                data.clear()
                data.append(row[0])
                data.append(row2[0])
                data.append(row[1])
                data.append(row2[1])
                data.append(len(row[1]))
                data.append(len(row2[1]))
                distanced=distance(row[1], row2[1])
                data.append(distanced)
                if len(row2[1]) == 0:
                    quotiant = 0
                else:
                    quotiant = (1 - (distanced / max(len(row[1]), len(row2[1])))) * 100
                if quotiant>50:
                    data.append(quotiant)
                    writer.writerow(data)



