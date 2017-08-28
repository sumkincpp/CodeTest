

REM ipv6 ip <-> MAC association
REM same as `ip -6 neigh show` in linux
netsh int ipv6 show neigh

REM Possible fix for ipv6 tcp/ip stack issues
netsh int ip reset
netsh winsock reset


REM Additional flush/reset options
netsh interface ipv6 reset
netsh advfirewall reset

REM disabling Teredo tunnel 
netsh int ipv6 isatap set state disabled
netsh int ipv6 6to4 set state disabled
netsh int teredo set state disabled

REM resetting full stack
ipconfig /flushdns
nbtstat -R
nbtstat -RR
netsh int reset all
netsh int ip reset
netsh winsock reset
