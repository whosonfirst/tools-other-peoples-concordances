#!/usr/bin/env python

import os
import sys

import csv

if __name__ == '__main__':

    dump = sys.argv[1]
    fh = open(dump, 'r')

    writer = csv.writer(sys.stdout)
    writer.writerow(('wd:id', 'gn:id'))

    wdid = None
    gnid = None

    for ln in fh:

        ln = ln.strip()

        if ln.startswith("wd:"):

            parts = ln.split(" ")
            parts = parts[0].split(":")

            wdid = parts[1]
            continue

        if not wdid:
            continue

        if ln.startswith("ps:P1566"):

            parts = ln.split(" ")
            gnid = parts[1]
            
            gnid = gnid.rstrip('"')
            gnid = gnid.lstrip('"')

            # print "%s %s" % (wdid, gnid)

            out = (wdid, gnid)
            writer.writerow(out)

            wdid = None
            gnid = None


            

