#!/usr/bin/env python

"""
Convert the quattroshapes_gazetteer_gp_then_gn.shp/geojson file (which is 1.3GB)
in to a smaller friendly CSV file (which is only... 27MB)

"""

import sys
import logging
import geojson
import csv

if __name__ == '__main__':

    dump = sys.argv[1]
    fh = open(dump, 'r')

    data = geojson.load(fh)

    writer = csv.DictWriter(sys.stdout, fieldnames=('qs:id', 'gn:id', 'gp:id'))
    writer.writeheader()

    for feature in data['features']:

        props = feature['properties']

        qsid = props.get('qs_id', 0)
        gnid = props.get('gn_id', 0)
        gpid = props.get('woe_id', 0)

        out = {
            'qs:id': qsid,
            'gn:id': gnid,
            'gp:id': gpid
        }

        writer.writerow(out)

        
