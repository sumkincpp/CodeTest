Usually it's located here "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" 

**Allowing Execution for PS script**
```
Set-ExecutionPolicy RemoteSigned
```
OR
```
powershell -ExecutionPolicy ByPass -File script.ps1
```

**Sleep for 10 seconds**
```
Start-Sleep -s 10
```
