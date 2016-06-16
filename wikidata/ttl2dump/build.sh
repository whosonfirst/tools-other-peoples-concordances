#!/bin/sh

CWD=`pwd`

export GOPATH="${ROOT}"
export GOARCH='amd64'

for OS in darwin windows linux
do 
	
    export GOOS="${OS}"
    
    echo "build ttl2dump for ${OS}"
    go build -o bin/${OS}/ttl2dump cmd/ttl2dump.go
done

exit 0

