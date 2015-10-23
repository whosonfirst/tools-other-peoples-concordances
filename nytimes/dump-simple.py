#!/usr/bin/env python

"""
Take the output of dump-locations.py and massage it in to a simple <NS>:id and <ID> CSV
file without all the semantic web / fully qualified URL hoohah
"""

import os
import logging
import csv
import sys
import urlparse

if __name__ == '__main__':

    dump = sys.argv[1]
    fh = open(dump, 'r')

    reader = csv.DictReader(fh)
    writer = None

    shortnames = {
        'data.nytimes.com': 'nyt:id',
        'sws.geonames.org': 'gn:id',
        'dbpedia.org': 'dbp:id',
        'rdf.freebase.com': 'fb:id',
        }
    
    for row in reader:

        out = {}

        for k, v in row.items():

            info = urlparse.urlparse(v)
            whoami = info.netloc

            k = shortnames.get(k, k)

            if k == "":
                out[k] = ""

            if whoami == 'data.nytimes.com':
                fname = os.path.basename(v)
                fname = fname.replace(".rdf", "")
                id = fname

            elif whoami == 'sws.geonames.org':
                v = v.rstrip("/")
                fname = os.path.basename(v)
                id = fname
                out[k] = id
                
            elif whoami == 'dbpedia.org':
                fname = os.path.basename(v)
                id = fname
                
            elif whoami == 'rdf.freebase.com':
                fname = os.path.basename(v)
                id = fname
                
            else:
                id = v

            out[k] = id

        if not writer:
            writer = csv.DictWriter(sys.stdout, fieldnames=out.keys())
            writer.writeheader()

        writer.writerow(out)
