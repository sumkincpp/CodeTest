

# similar to netstat command, but it returns an oject instead of a string.
Get-NetTCPConnection -State Listen | ft state,l*port, l*address, r*port, r*address –Auto
