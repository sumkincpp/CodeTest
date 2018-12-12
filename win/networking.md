
# windows routes
route print
netstat -rn


netsh interface ipv4 show interfaces
netsh interface ip show config
netsh interface show interface

netsh interface ip set address name="Local Area Connection" static 192.168.10.42 255.255.255.0 192.168.1.1
netsh interface ip set dns "Local Area Connection" static 192.168.1.1
netsh interface ip add dns name="Local Area Connection" 208.67.220.220 index=2

netsh interface ip set wins "Local Area Connection" static 192.168.1.1

netsh interface ip set address "Local Area Connection" dhcp
netsh interface ip set dns "Local Area Connection" dhcp
netsh interface ip set dnsservers name="Local Area Connection" source=dhcp

Clear DNS servers:
wmic nicconfig where (IPEnabled=TRUE) call SetDNSServerSearchOrder ()

Set 1 DNS server:
wmic nicconfig where (IPEnabled=TRUE) call SetDNSServerSearchOrder ("8.8.8.8")

Set 2 DNS servers:
wmic nicconfig where (IPEnabled=TRUE) call SetDNSServerSearchOrder ("8.8.8.8", "8.8.4.4")

Set 2 DNS servers on a particular network adapter:
wmic nicconfig where "(IPEnabled=TRUE) and (Description = 'Local Area Connection')" call SetDNSServerSearchOrder ("8.8.8.8", "8.8.4.4")

Another example for setting the domain search list:
wmic nicconfig call SetDNSSuffixSearchOrder ("domain.tld")
