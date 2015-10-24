vi /etc/pf.conf 

++ add something like

```
# added by fedor
#   sudo pfctl -f /etc/pf.conf && sudo pfctl -e
ext_if="en0" # interface connected to internet

table <allowedips> persist file "/etc/pf.allowed.ip.conf"
table <blockedips> persist file "/etc/pf.blocked.ip.conf"

block return-rst in log (all) quick on $ext_if proto TCP from <blockedips> to any
  pass in log (all) quick on $ext_if from <allowedips> to any
  pass out log (all) quick on $ext_if from any to <allowedips>
```

Create /etc/pf.allowed.ip.conf && /etc/pf.blocked.ip.conf and fill with blocked outbound nets.

To reload :

    sudo pfctl -f /etc/pf.conf && sudo pfctl -e
    
