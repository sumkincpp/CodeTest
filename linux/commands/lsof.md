## Tested on MAC OS X, actually

lsof process with pid X, hosts not resolved(-n), ports also unresolved(-P) 
```
lsof -n -P -p X
```

TCP sessions + listeners, hosts not resolved(-n), ports also unresolved(-P)
```
lsof -n -P -iTCP
```

Also TCP:LISTEN entries :
```
sudo lsof -iTCP -sTCP:LISTEN -P -n
```

UDP listeners, hosts not resolved(-n), ports also unresolved(-P)
```
lsof -n -P -iUDP
```

lsof :80 port
```
sudo lsof -i :80 -n -P
```

lsof files used in directory /var/log
```
sudo lsof -n  +D /var/log
```

lsof + perl: counting Descriptors by groups ("<process_name>:<process_pid>")
```
sudo lsof -n -P | perl -lane '$x{"$F[0]:$F[1]"}++; END { print "$x{$_}\t$_" for sort {$x{$a}<=>$x{$b}} keys %x}';
```


