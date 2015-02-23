# Mounting / remounting in single mode

# passwd root
Changing password for user root.
New UNIX password:
Retype new UNIX password:
passwd: Authentication token lock busy 

>>>

mount -o ro /proc
mount -o remount,rw /
