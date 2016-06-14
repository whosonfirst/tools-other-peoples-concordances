package main

import (
       "bufio"
	"compress/bzip2"
	"flag"
	"fmt"
	"os"
)


func main() {

     ttl := flag.String("ttl", "", "...")

     flag.Parse()

	fh, err := os.Open(*ttl)

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
