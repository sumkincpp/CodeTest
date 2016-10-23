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
