
```
net stop named
net start named
```

# Powershell

```
Get-Service | Where-Object {($_.status -eq "stopped") -and ($_.StartType -eq "Automatic")}

Restart-Service btwdins,alerter
Restart-Service -displayname "bluetooth service"

Start-Service btwdins
Stop-Service btwdins
```
