dump:
	./ttl2dump/bin/linux/ttl2dump -ttl wikidata-latest.ttl.bz2 | grep "$(PROP) " | grep -v wdt > $(PROP).txt
	./dump2csv.py -i $(PROP) $(PROP).txt > $(PROP).csv

geonames:
	$(MAKE) dump PROP=P1566
	mv P238.csv wikidata-geonames.csv

airports: iata icao faa

iata:
	$(MAKE) dump PROP=P238
	mv P238.csv wikidata-iata.csv

icao:
	$(MAKE) dump PROP=P239
	mv P239.csv wikidata-icao.csv

faa:
	$(MAKE) dump PROP=P240
	mv P240.csv wikidata-faa.csv
