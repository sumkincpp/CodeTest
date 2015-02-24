#!/bin/bash
export done=1;
 
while [ $done -gt 0 ]; do
    /usr/bin/curl -O -C - $1;
    export done=$?;
done
 
if [ $done -eq 0 ]; then
    echo "Downloaded $1";
fi
