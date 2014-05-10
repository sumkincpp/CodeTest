sudo ip link add link eth0 macvlan0 type macvlan
sudo ifconfig macvlan0 up
sudo dhclient macvlan0
sudo ip route add default via 192.168.1.1 
