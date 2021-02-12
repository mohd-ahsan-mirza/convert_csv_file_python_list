#!/usr/bin/python
import sys
import csv

if len(sys.argv) == 2:
    if sys.argv[1].endswith('.csv'):
        filename = sys.argv[1]
        data = list()
        with  open(filename, 'r', encoding='utf-8-sig') as data:  
            reader = csv.DictReader(data)
            data = list(reader)
        print(data)
    else:
        print("Pass in a file that has a csv extension")
else:
    print("Pass in the csv filename with the absolute path")
