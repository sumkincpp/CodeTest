# startup applications
wmic startup


wmic useraccount list
wmic group list full

wmic csproduct get uuid
wmic csproduct get name
wmic csproduct get vendor,name,identifyingnumber

wmic diskdrive get status
wmic bios get serialnumber
wmic logicaldisk get name, volumename
wmic Memcache list brief

wmic ComputerSystem get TotalPhysicalMemory

wmic OS get TotalVirtualMemorySize

wmic product get name

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
wmic CPU get NumberOfLogicalProcessors
wmic CPU get NumberOfCores

# motherboard

wmic baseboard get manufacturer
wmic baseboard get product
wmic baseboard get version
