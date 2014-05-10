sudo ip link add link eth0 mac0 type macvlan
sudo ifconfig mac0 up
sudo dhclient mac0
sudo ip route add default via 192.168.1.1 
