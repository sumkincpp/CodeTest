# 1. Check current screen resolution
$ xrandr | grep '*'
1280x800       59.9*+

# 2. Connect to RDP PC
$ xfreerdp --plugin cliprdr -g 1280x800 -d <domain> -u <login> <ip/host>
loading plugin cliprdr
connected to 172.20.0.145:3389
Password: 
Failed to check xfreerdp file descriptor

# Ctrl + Alt + Enter --- Enter/Exit full screen

