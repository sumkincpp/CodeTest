

REM ipv6 ip <-> MAC association
REM same as `ip -6 neigh show` in linux
netsh int ipv6 show neigh

REM Possible fix for ipv6 tcp/ip stack issues
netsh int ip reset
netsh winsock reset
