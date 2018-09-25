
### winver (GUI)

winver.exe

### CMD
```
C:\>ver

Microsoft Windows [Version 10.0.17134.285]
```

### Powershell 1

```
PS C:\> [Environment]::OSVersion

Platform ServicePack Version      VersionString
-------- ----------- -------      -------------
 Win32NT             10.0.17134.0 Microsoft Windows NT 10.0.17134.0
```

### Powershell 2

```
C:\> Get-ItemProperty -Path "HKLM:\Software\Microsoft\Windows NT\CurrentVersion"


SystemRoot                : C:\Windows
BuildBranch               : rs4_release
BuildGUID                 : ffffffff-ffff-ffff-ffff-ffffffffffff
BuildLab                  : 17134.rs4_release.180410-1804
BuildLabEx                : 17134.1.amd64fre.rs4_release.180410-1804
CompositionEditionID      : Enterprise
CurrentBuild              : 17134
CurrentBuildNumber        : 17134
CurrentMajorVersionNumber : 10
CurrentMinorVersionNumber : 0
CurrentType               : Multiprocessor Free
CurrentVersion            : 6.3
EditionID                 : Professional
EditionSubManufacturer    :
EditionSubstring          :
EditionSubVersion         :
InstallationType          : Client
InstallDate               : 1531894630
ProductName               : Windows 10 Pro
ReleaseId                 : 1803
SoftwareType              : System
UBR                       : 285
PathName                  : C:\Windows
ProductId                 : 00330-50000-00000-AAOEM
DigitalProductId          : {164, 0, 0, 0...}
DigitalProductId4         : {248, 4, 0, 0...}
RegisteredOwner           : fedor
RegisteredOrganization    :
InstallTime               : 131763682306027856
PSPath                    : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\Software\Microsoft\Windows
                            NT\CurrentVersion
PSParentPath              : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT
PSChildName               : CurrentVersion
PSDrive                   : HKLM
PSProvider                : Microsoft.PowerShell.Core\Registry

```
