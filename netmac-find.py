__author__ = 'misaflansb'

# Will use tailored .csv for this one

import csv


# read MAC addresses from .csv file into iterable list

maclist = []

with open('MAC.CSV', 'rb') as mac_csv:
    macreader = csv.reader(mac_csv, delimiter='\n')
    for row in macreader:
        for i in row:
            i = ':'.join(i[e:e+2] for e in range(0,6,2))
            maclist.append(i)

with open('WING.log', 'rb') as logfile:
    for mac_segment in maclist:
        if mac_segment in logfile.read():
            print "This macsegment, {0}, was found".format(mac_segment)

logfile.close()