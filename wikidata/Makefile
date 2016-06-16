dump:
	./ttl2dump/bin/linux/ttl2dump -ttl wikidata-latest.ttl.bz2 | grep $(PROP) | grep -v wdt > $(PROP).txt
	./dump2csv.py -i $(PROP) > $(PROP).csv
