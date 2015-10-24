#!/usr/bin/env python

import sys
import csv

dump = sys.argv[1]
fh = open(dump, 'r')

reader = csv.DictReader(fh)
writer = None

for row in reader:

    out = {
        'gp:id': row['geoplanet'],
        'fct:id': row['factual'],
        'gn:id': row['geonames']
    }

    if not writer:
        writer = csv.DictWriter(sys.stdout, fieldnames=out.keys())
        writer.writeheader()

    writer.writerow(out)
