# netmac-find

Looking for MAC address based on IEEE manufacturer MAC schema. 

Currently the MAC.CSV file contains all Apple MACs (manufacturer ID portion).
The MAC.CSV has been stripped of extraneous columns. Will likely later want to 
be able to read the standard export .csv file from [IEEE Registration Authority page](https://regauth.standards.ieee.org/standards-ra-web/pub/view.html#registries).

In our environment we were searching through our wireless controller's log file that it sent to our central
syslog server. Since all Apple devices on our network connect wirelessly, we would be able to see them when they
associate with the various access points (AP) managed by our WING wireless controller.

Add your log file in any format, keeping in mind you may want to alter this bit as needed (line 16):

`i = '-'.join(i[e:e+2] for e in range(0,6,2))`