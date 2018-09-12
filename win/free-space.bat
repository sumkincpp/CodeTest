

dir|find "bytes free"

wmic /node:"%COMPUTERNAME%" LogicalDisk Where DriveType="3" Get DeviceID,FreeSpace|find /I "c:"

REM requires admin
fsutil volume diskfree c:
