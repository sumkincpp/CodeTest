# fully `netstat -abno` on powershell
#
# Get-NetTCPConnection
# https://technet.microsoft.com/en-us/library/hh826153.aspx
#
# MSFT_NetTCPConnection, ROOT\StandardCimv2
# http://wutils.com/wmi/root/standardcimv2/msft_nettcpconnection/
#
# Where-Object -Property State -EQ -Value 'Established'
Get-NetTCPConnection | ForEach-Object -Process {
    $process = (Get-Process -Id $_.OwningProcess)
    [PSCustomObject] @{
        'Local Address' = $_.LocalAddress
        'LocalPort'     = $_.LocalPort
        'RemoteIP'      = $_.RemoteAddress
        'RemotePort'    = $_.RemotePort
        'ProcessId'     = $process.Id
        'ProcessName'   = $process.Name
        'State'         = $_.State
    }
} | Sort-Object State -descending
