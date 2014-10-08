
# Sending udp packet with "foo" payload
echo -n "foo" | nc -4u -w1 127.0.0.1 9001
