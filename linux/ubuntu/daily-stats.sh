#!/bin/bash

set -e
set -o pipefail

title() { echo; echo ====== $@ =======; echo; }

title sysinfo
landscape-sysinfo

title Memory
free -m

title Remaining Space
df -h

title Any Updates?
/etc/update-motd.d/90-updates-available

title Listening
sudo netstat -laputen

title Connections
sudo netstat -net

title Processes
sudo ps aux

title Docker Containers
docker ps -a

title Docker Images
docker images
