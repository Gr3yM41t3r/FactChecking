from Levenshtein import distance
import csv
edit_dist = distance("Mitt Romney says Barack Obama 'could have gotten crippling sanctions against Iran. He did not.'", "Paul Ryan says the Obama administration ‘watered down sanctions’ against Iran")
print(edit_dist)
header = ['TextA', 'TextB', 'IdA', 'IdB', 'Levenshtein-Distance']
data = []

with open("small_claimskg_result.csv") as f:
    reader = csv.reader(f)
    myData = list(reader)
    with open('similarity.csv', 'w') as g:
        writer = csv.writer(g)
        writer.writerow(header)
        for row in myData:
            for row2 in myData:
                data.clear()
                data.append(row[1])
                data.append(row2[1])
                data.append(row[0])
                data.append(row2[0])
                data.append(distance(row[1], row2[1]))
                writer.writerow(data)

