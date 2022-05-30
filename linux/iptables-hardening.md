https://www.ibm.com/docs/en/linux-on-systems?topic=tests-firewall-iptables-rules


# Firewall 2

```
The rules we used for firewall 2 were:
Stop all incoming traffic using the following command:
iptables -P INPUT DROP

Allow SSH session to firewall 2 by using the following command:
iptables -A INPUT -p tcp --dport 22 -s 0/0 -j ACCEPT

Allow ICMP traffic to firewall 2 by using the following command:
iptables -A INPUT -p icmp -j ACCEPT

Allow all related and established traffic for firewall 2 by using the following command:
iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT

Stop all forwarding by using the following command:
iptables -P FORWARD DROP

Allow forwarding of TCP traffic on IP interface 10.10.60.0 (client) port 80 (HTTP) and port 443 (HTTPS) to go to 192.168.40.95 (webApp.secure) by using the following commands:
iptables -A FORWARD -p tcp --dport 80 -s 10.10.60.0/24 -d 192.168.40.95 -j ACCEPT

iptables -A FORWARD -p tcp --dport 443 -s 10.10.60.0/24 -d 192.168.40.95 -j ACCEPT

Allow forwarding of ICMP traffic by using the following command:
iptables -A FORWARD -p icmp -j ACCEPT

Allow forwarding of all related and established traffic by using the following command:
iptables -A FORWARD -m state --state RELATED,ESTABLISHED -j ACCEPT

Allow output traffic for ICMP by using the following command:
iptables -A OUTPUT -p icmp -j ACCEPT
```

# Firewall 1

```
The rules we used for firewall 1 were:
Stop all incoming traffic by using the following command:
iptables -P INPUT DROP

Allow SSH session to firewall 1 by using the following command:
iptables -A INPUT -p tcp --dport 22 -s 0/0 -j ACCEPT

Allow ICMP traffic to firewall 1 by using the following command:
iptables -A INPUT -p icmp -j ACCEPT

Allow all related and established traffic for firewall 1 by using the following command:
iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT

Stop all forwarding by using the following command:
iptables -P FORWARD DROP

Allow forwarding of TCP traffic on interface 192.168.40.0 (guest LAN) to go to 10.10.50.110 (HiperSockets™ to z/OS®) by using the following command:
iptables -A FORWARD -p tcp -i hsi1 -o hsi2 -d 10.10.50.110 -j ACCEPT

Allow forwarding of ICMP traffic by using the following command:
iptables -A FORWARD -p icmp -j ACCEPT

Allow forwarding of all related and established traffic by using the following command:
iptables -A FORWARD -m state --state RELATED,ESTABLISHED -j ACCEPT

Allow output traffic for ICMP by using the following command:
iptables -A OUTPUT -p icmp -j ACCEPT
```
