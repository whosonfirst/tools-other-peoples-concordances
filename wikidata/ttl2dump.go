package main

import (
       "bufio"
	"compress/bzip2"
	"fmt"
	"os"
)


func main() {

	fname := "wikidata-20160509-all-BETA.ttl.bz2"

	fh, err := os.Open(fname)

	if err != nil {
		panic(err)
	}

	defer fh.Close()

	bz := bzip2.NewReader(fh)

	buf := bufio.NewScanner(bz)

	for buf.Scan(){
	    fmt.Println(buf.Text())
	}
}
