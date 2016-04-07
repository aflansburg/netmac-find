__author__ = 'misaflansb'

# Will use tailored .csv for this one

import csv


# read MAC addresses from .csv file into iterable list

maclist = []

with open('MAC.CSV', 'rb') as mac_csv:
    macreader = csv.reader(mac_csv, delimiter='\n')
    for row in macreader:
        for i in row:
            maclist.append(i)


