import csv

#number_of_claims = sum(1 for row in csvreader)

false = 0
other = 0
true = 0
mixture = 0
with open("claimskg_result.csv") as f:
    reader = csv.reader(f)
    myData = list(reader)
    for row in myData:
        list1 = row[9].split()
        # print(list1)
        for row2 in myData:
            list2 = row2[9].split()
            # print(list2)
            list_as_list1 = set(list1)
            intersection = list_as_list1.intersection(list2)
            intersection_as_list = list(intersection)
            print(intersection_as_list)
##'''
list1 = ["amie", "amine", "ami"]
list2 = ["aemine", "amine", "addmieee"]
list_as_lis1 = set(list1)
intersection = list_as_lis1.intersection(list2)
intersection_as_list = list(intersection)
print(intersection_as_list)
