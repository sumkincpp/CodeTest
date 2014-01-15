
# Basic configuration SeLinux/iptables

# Disabling firewall

service iptables save
service iptables stop
chkconfig iptables off

OR

service iptables start
chkconfig iptables on
