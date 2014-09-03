
import sys, os

for fn in os.listdir('.'):
    if not fn.endswith('csv'): continue
    print fn
    for line in open(fn):
        col = line.strip().split(';')
        if len(col) > 3:
            name = col[3]
            date = col[1]
            amount = col[-1].replace(',', '.')
            print name + '\t' + date + '\t\t' + amount

