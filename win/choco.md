

List packages that will be upgraded
```
choco upgrade all --noop -y
```

Upgraded packages without prompting
```
choco upgrade all -y
```

freeze/pin dependency 
```
choco pin
choco pin list
choco pin add -n=git
choco pin add -n=git --version 1.2.3
choco pin remove --name git
```
