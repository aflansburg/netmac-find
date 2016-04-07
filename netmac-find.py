__author__ = 'misaflansb'

# Will use tailored .csv for this one

import csv, mmap
import re

# read MAC addresses from .csv file into iterable list

maclist = []

with open('MAC.CSV', 'rb') as mac_csv:
    macreader = csv.reader(mac_csv, delimiter='\n')
    for row in macreader:
        for i in row:
            i = '-'.join(i[e:e+2] for e in range(0,6,2))
            maclist.append(i)

mac_csv.close()

# find and store MAC segments in a list from file using mmap (memory mapped file)

mac_addresses = []

with open('WING.log', "r+b") as log_file:
    s = mmap.mmap(log_file.fileno(), 0, prot=mmap.PROT_READ)
    for line in iter(s.readline, ""):
        for mac in maclist:
            if mac in line:
                regex = r'(' + re.escape(mac) + r'.{9})'
                g = re.search(regex, line, re.IGNORECASE)
                if g.group(1) not in mac_addresses:
                    mac_addresses.append(g.group(1))
                    print "Adding {0} to mac_addresses list.".format(g.group(0))

log_file.close()

print "There are {0} unique Apple devices that have " \
      "connected to Wireless in the last month.".format(len(mac_addresses))

with open("mac_output.csv", "wb") as out_file:
    csv_writer = csv.writer(out_file)
    for e in mac_addresses:
        csv_writer.writerow([e])


print "mac_addresses written to csv file: {0}".format(out_file.name)

out_file.close()