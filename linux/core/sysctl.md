# reload sysctl.conf
systcl -p

# Reload settings from all system configuration files (also from /etc/sysctl.d/* )
sysctl --system

# Disable ipv6
```
sysctl -w net.ipv6.conf.all.disable_ipv6=1
sysctl -w net.ipv6.conf.default.disable_ipv6=1
```

*sysctl.conf*
```
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1
```
