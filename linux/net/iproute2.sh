# ip link list
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 16436 qdisc noqueue
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast qlen 1000
    link/ether 00:50:56:95:ea:7b brd ff:ff:ff:ff:ff:ff

# ip route
192.168.100.0/24 dev eth0  proto kernel  scope link  src 192.168.100.30
169.254.0.0/16 dev eth0  scope link
default via 192.168.100.20 dev eth0
