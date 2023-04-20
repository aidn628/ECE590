import csv

with open('testfile.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

for row in data:
    print(row)
    print(type(float(row[0])))