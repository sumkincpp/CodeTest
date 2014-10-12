
# Sending udp packet with "foo" payload
echo -n "foo" | nc -4u -w1 127.0.0.1 9001

# port scan network :D
for i in {21..29}; do nc -v -n -z -w 1 192.168.0.$i 443; done
