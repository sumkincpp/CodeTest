fedor@Fedors-MacBook-Pro:~/Code/SNMP/net-snmp/net-snmp-mib2$ snmpwalk -c public localhost:1161 .1.3.6.1.2.1 | sed 's/\([\w-]*-MIB\).*/\1/' | uniq
SNMPv2-MIB
DISMAN-EVENT-MIB
SNMPv2-MIB
IF-MIB
SNMPv2-SMI::mib-2.3.1.1.1.4.1.192.168.40.1 = INTEGER: 4
SNMPv2-SMI::mib-2.3.1.1.1.4.1.192.168.40.36 = INTEGER: 4
SNMPv2-SMI::mib-2.3.1.1.2.4.1.192.168.40.1 = Hex-STRING: 40 4A 03 77 68 07
SNMPv2-SMI::mib-2.3.1.1.2.4.1.192.168.40.36 = Hex-STRING: 18 34 51 01 68 75
SNMPv2-SMI::mib-2.3.1.1.3.4.1.192.168.40.1 = IpAddress: 192.168.40.1
SNMPv2-SMI::mib-2.3.1.1.3.4.1.192.168.40.36 = IpAddress: 192.168.40.36
IP-MIB
TCP-MIB
UDP-MIB
SNMPv2-MIB
HOST-RESOURCES-MIB
IF-MIB
DISMAN-EVENT-MIB
NOTIFICATION-LOG-MIB
