import csv

file = open('claimskg_result.csv')
csvreader = csv.reader(file)

number_of_claims = sum(1 for row in csvreader)

false = 0
other = 0
true = 0
mixture = 0
with open("claimskg_result.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        list1 = row[9].split()
        # print(list1)
        list2 = row[9].split()
        # print(list2)
        list_as_lis1 = set(list1)
        intersection = list_as_lis1.intersection(list2)
        intersection_as_list = list(intersection)
        print(intersection_as_list)
##'''
list1 = ["amie", "amine", "ami"]
list2 = ["aemine", "amine", "a
ddmieee"]
s
list_as_lis1 = set(list1)
intersection = list_as_lis1.intersection(list2)
intersection_as_list = list(intersection)
print(intersection_as_list)
