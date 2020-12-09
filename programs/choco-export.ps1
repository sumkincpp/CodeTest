$packageXml = ''
choco list -lo -r | % { $_ -split '\|' | select -first 1 } | % { $packageXml += "`n    <package Id=""$_"" />" }
Set-Content -Path packages.config -Value "<packages>$packageXml`n</packages>"

# import
# choco install packages.config
