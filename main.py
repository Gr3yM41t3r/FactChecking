import csv

file = open('claimskg_result.csv')
csvreader = csv.reader(file)

number_of_claims = sum(1 for row in csvreader)
print(number_of_claims)
