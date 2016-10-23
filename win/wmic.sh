# startup applications
wmic startup

wmic useraccount list
wmic group list full

wmic diskdrive get status
wmic bios get serialnumber
wmic logicaldisk get name, volumename
wmic Memcache list brief

wmic ComputerSystem get TotalPhysicalMemory
wmic computersystem get TotalPhysicalMemory /VALUE /FORMAT:VALUE

# csproduct

wmic csproduct get uuid
wmic csproduct get name
wmic csproduct get vendor,name,identifyingnumber

# OS

wmic OS get TotalVirtualMemorySize
wmic os get freephysicalmemory /VALUE /FORMAT:VALUE
wmic OS Get LastBootUpTime | findstr +

# product

wmic product get name
wmic product where "name like '%%ProgramName%%'" call uninstall /nointeractive

wmic useraccount where name='Administrator' call Rename admin

# list brief

wmic product list brief | sort
wmic service list brief | sort
wmic process list brief | sort
wmic startup list brief | sort

# net things

wmic netlogin list full /format:htable
wmic LOGON list full /format:htable
wmic netuse list full /format:htable

# process

wmic process get name,executablepath
wmic process where "name like '%java%'" delete
wmic process get CSName,Description,ExecutablePath,ProcessId 
wmic process get name,pagefileusage,virtualsize,workingsetsize,usermodetime,kernelmodetime,ThreadCount /format:csv
wmic process where name="cmd.exe" CALL setpriority "below normal"

# cpu

wmic cpu list brief
wmic cpu get name
wmic cpu get name /Value
wmic CPU get NumberOfLogicalProcessors
wmic CPU get NumberOfCores
wmic cpu get loadpercentage /VALUE /FORMAT:VALUE

# motherboard

wmic baseboard get manufacturer
wmic baseboard get product
wmic baseboard get version

# path

wmic path win32_networkadapter where index=0 call disable
wmic path win32_networkadapter where index=0 call enable

wmic path win32_battery get batterystatus 
wmic path win32_battery get estimatedchargeremaining

WMIC PATH WIN32_USERACCOUNT WHERE LOCALACCOUNT=TRUE get caption
wmic path Win32_UserAccount get /ALL /FORMAT:list

wmic path Win32_Desktop get /ALL /FORMAT:list

wmic path win32_registry get /?
