__author__ = 'misaflansb'

# Will use tailored .csv for this one

import csv
import mmap

# read MAC addresses from .csv file into iterable list

maclist = []

with open('MAC.CSV', 'rb') as mac_csv:
    macreader = csv.reader(mac_csv, delimiter='\n')
    for row in macreader:
        for i in row:
            i = '-'.join(i[e:e+2] for e in range(0,6,2))
            maclist.append(i)

confirmed_mac = []

read_file = open('WING.log')
s = mmap.mmap(read_file.fileno(), 0, access=mmap.ACCESS_READ)

for mac_segment in maclist:
    if s.find(mac_segment) != -1:
            print "This macsegment, {0}, was found".format(mac_segment)
            confirmed_mac.append(mac_segment)