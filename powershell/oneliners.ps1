

# similar to netstat command, but it returns an oject instead of a string.
Get-NetTCPConnection -State Listen | ft state,l*port, l*address, r*port, r*address –Auto

# Current Hostname
$env:computername
Hostname
(Get-WmiObject -Class Win32_ComputerSystem -Property Name).Name
get-childitem -path env:computername

PS C:/> (Get-Date).ToString("yyyyMMdd")
20161202

# Random pasword 
> -join((("abcdefghiklmnoprstuvwxyzABCDEFGHKLMNPRSTUVWXYZ123456789".ToCharArray()|Get-Random -Count 8) + ("1234567890".ToCharArray()|Get-Random -Count 2) + ('!"§$%&/()=?}][{@#*+'.ToCharArray()|Get-Random -Count 1) ) | Sort-Object {Get-Random})
