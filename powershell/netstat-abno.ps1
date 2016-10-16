# fully `netstat -abno` on powershell

Get-NetTCPConnection | ForEach-Object -Process {
    [PSCustomObject] @{
        'ProcessName' = (Get-Process -Id $_.OwningProcess).Name
        'ProcessId' = (Get-Process -Id $_.OwningProcess).Id
        'RemoteIP'  = $_.RemoteAddress
        'LocalPort' = $_.LocalPort
        'State'     = $_.State
    }
}
