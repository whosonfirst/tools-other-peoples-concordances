#!/usr/bin/python

"""
Take the freak-show RDF file that the NYT publishes and export it as a simple CSV
file (full of fully-qualified URLS...)
"""

import sys
import csv
import logging

import urlparse
import elementtree.ElementTree as ET

if __name__ == '__main__':

    others = { "data.nytimes.com": 0 }
    places = []

    dump = sys.argv[1]

    tree = ET.parse(dump)
    root = tree.getroot()

    for desc in root.findall('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}Description'):

        about = desc.attrib['{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about']
        info = urlparse.urlparse(about)

        whoami = info.netloc

        # only dump top-level NYT things

        if whoami != 'data.nytimes.com':
            # logging.error("WHO IS %s" % whoami)
            continue

        others[ whoami ] += 1
        place = { whoami : about }

        for same in desc.findall('{http://www.w3.org/2002/07/owl#}sameAs'):

            other = same.attrib['{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource']

            info = urlparse.urlparse(other)
            source = info.netloc

            if source == 'data.nytimes.com':
                continue

            place[ source ] = other

        places.append(place)

        count = others.get(source, 0)
        count += 1

        others[source] = count

    writer = csv.DictWriter(sys.stdout, fieldnames=others.keys())
    writer.writeheader()

    for pl in places:

        out = {}

        for k, ignore in others.items():
            out[k] = ""

        for k, v in pl.items():
            out[k] = v

        writer.writerow(out)

