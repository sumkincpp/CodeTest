# Provides list of started services
net start

# Get list of currently running tasks
tasklist /svc

# Disable/enable services
msconfig

# Get list of currently listening services
netstat -ano

# Flush dat DNS-es!
ipconfig /flushdns

# --------------------------------------------------
ipconfig /all
ipconfig /renew
systeminfo
arp -a
whoami

# Windows GUI consoles
lusrmgr.msc   # Local User Manager Gui 
control       # Control Panel 
secpol.msc    # Local Security Policy for firewalls, Accounts, etc
eventvwr.msc  # Event Viewer
