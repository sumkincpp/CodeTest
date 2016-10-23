PS C:\Users\user> Get-CimClass *Process | select CimClassName | ft

CimClassName
------------
CIM_Process
Win32_Process
Win32_SessionProcess
Win32_NamedJobObjectProcess
CIM_OSProcess
Win32_PerfFormattedData_PerfProc_Process
Win32_PerfRawData_PerfProc_Process

# ------------------------------------------------------------------------------------------------------------------------

PS C:\Users\user> Get-WmiObject -Class Win32_OperatingSystem | select LastBootUpTime

LastBootUpTime
--------------
20161012201716.528901+180

# ------------------------------------------------------------------------------------------------------------------------

PS C:\Users\user> Get-WmiObject -Class Win32_OperatingSystem | select @{N=’LastBootTime’; E={$_.ConvertToDateTime($_.LastBootUpTime)}}

LastBootTime
------------
12.10.2016 20:17:16

# ------------------------------------------------------------------------------------------------------------------------

PS C:\Users\user> Get-CimInstance -ClassName Win32_OperatingSystem | select LastBootUpTime

LastBootUpTime
--------------
12.10.2016 20:17:16

# ------------------------------------------------------------------------------------------------------------------------

PS C:\Users\user> Get-CimInstance -ClassName Win32_Process | select *time  -last 1

KernelModeTime UserModeTime
-------------- ------------
             0       156250

# ------------------------------------------------------------------------------------------------------------------------

PS C:\Users\user>  Get-WmiObject -Class Win32_Process | Get-Member -MemberType Method


   TypeName: System.Management.ManagementObject#root\cimv2\Win32_Process

Name                    MemberType Definition
----                    ---------- ----------
AttachDebugger          Method     System.Management.ManagementBaseObject AttachDebugger()
GetAvailableVirtualSize Method     System.Management.ManagementBaseObject GetAvailableVirtualSize()
GetOwner                Method     System.Management.ManagementBaseObject GetOwner()
GetOwnerSid             Method     System.Management.ManagementBaseObject GetOwnerSid()
SetPriority             Method     System.Management.ManagementBaseObject SetPriority(System.Int32 Priority)
Terminate               Method     System.Management.ManagementBaseObject Terminate(System.UInt32 Reason)

# ------------------------------------------------------------------------------------------------------------------------

PS C:\Users\user>  Get-CimInstance -ClassName Win32_Process | Get-Member -MemberType Method


   TypeName: Microsoft.Management.Infrastructure.CimInstance#root/cimv2/Win32_Process

Name                      MemberType Definition
----                      ---------- ----------
Clone                     Method     System.Object ICloneable.Clone()
Dispose                   Method     void Dispose(), void IDisposable.Dispose()
Equals                    Method     bool Equals(System.Object obj)
GetCimSessionComputerName Method     string GetCimSessionComputerName()
GetCimSessionInstanceId   Method     guid GetCimSessionInstanceId()
GetHashCode               Method     int GetHashCode()
GetObjectData             Method     void GetObjectData(System.Runtime.Serialization.SerializationInfo info, System....
GetType                   Method     type GetType()
ToString                  Method     string ToString()

# ------------------------------------------------------------------------------------------------------------------------

PS C:\Users\user> Get-CimInstance -ClassName Win32_Process -Filter "Name like 'notepad%'" | Invoke-CimMethod -MethodName Terminate
 
# ------------------------------------------------------------------------------------------------------------------------

PS C:\Users\user> Get-CimInstance -Query "SELECT * from Win32_Process WHERE name LIKE 'po%'"

ProcessId Name           HandleCount WorkingSetSize VirtualSize
--------- ----           ----------- -------------- -----------
13640     powershell.exe 606         89698304       2199726125056
2744      powershell.exe 679         82423808       2199716061184


