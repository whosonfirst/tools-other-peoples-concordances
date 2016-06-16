# wikidata

## Important

This isn't push button easy yet.

## Usage

You will need to have `Python` and the `bzip2` utility installed on your computer.

First you will need to grab the [Wikidata RDF dump](https://m.wikidata.org/wiki/Wikidata:Database_download). Make sure to get the "Turtle" formatted files.

```
wget https://dumps.wikimedia.org/wikidatawiki/entities/20160509/wikidata-20160509-all-BETA.ttl.bz2
```

This will take a while.

Next you will need to tease out the [Geonames](http://geonames.org) data as identified by the `P1566` property.

```
./ttl2dump/bin/linux/ttl2dump -ttl wikidata-20160509-all-BETA.ttl.bz2 | grep P1566 | grep -v wdt > P1566.txt
```

_[ttl2dump](ttl2dump) is a small utility written in [Go](http://golang.org) to stream the content of a bzip-encoded file so that you don't have to decompress the whole thing to start working with it because it is HUGE. There are pre-compiled binary versions of `ttl2dump` available for [OS X](ttl2dump/bin/darwin) and [Linux](ttl2dump/bin/linux) and [Windows](ttl2dump/bin/windows)._

This will also take a while. It is important to understand this is a lucky hack. The output of the above will look like this (until the Wikidata people change things...)

```
wd:Q4288651 p:P1566 wds:Q4288651-502F2A91-9708-410A-AE4A-AAD0E50E1164 .
    ps:P1566 "795250" ;
wd:Q4288670 p:P1566 wds:Q4288670-9713898B-4F44-442E-8608-88BFDAB618FB .
    ps:P1566 "625249" ;
```

Oh well, right? It's easier than trying to load 76GB of data in to a triple store.

Finally, parse the dump file in to a handy CSV file:

```
python dump2csv.py -i P1566 -l 'gn:id' P1566.txt > wikidata-geonames.csv
```

Rinse and repeat.
