
import csv
import sys

for line in csv.reader(open(sys.argv[1]), delimiter=';'):
    name = line[5] + ' | ' + line[4]
    date = line[1]
    amount = line[8].replace(',', '.')
    print name + '\t' + date + '\t\t' + amount

