#!/usr/bin/env python

import os
import sys

import csv

if __name__ == '__main__':

    import optparse
    opt_parser = optparse.OptionParser()

    opt_parser.add_option("-i", "--identifier", dest="identifier", default=None, help="...")
    opt_parser.add_option("-l", "--label", dest="label", default="other:id", help="...")

    options, args = opt_parser.parse_args()

    require = "ps:%s" % options.identifier

    dump = sys.argv[1]
    fh = open(dump, 'r')

    writer = csv.writer(sys.stdout)
    writer.writerow(('wd:id', options.label))

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

        if ln.startswith(require):

            parts = ln.split(" ")
            gnid = parts[1]
            
            gnid = gnid.rstrip('"')
            gnid = gnid.lstrip('"')

            # print "%s %s" % (wdid, gnid)

            out = (wdid, gnid)
            writer.writerow(out)

            wdid = None
            gnid = None


            

