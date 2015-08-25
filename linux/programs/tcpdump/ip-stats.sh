tcpdump -r capture-2015-08-25.pcap port 53 -nn | egrep -o '([0-9]*\.){3}([0-9])*' | sort | uniq -c | sort -n
