tcpdump -r capture-2015-08-25.pcap port 53 -nn | egrep -o ' [A-Za-z]([0-9A-Za-z\-]*\.){2,}' | sort | uniq -c | sort -n
