#!/bin/bash
logfile=$$.log
exec > $logfile 2>&1

#ORRRRRRRRR

#!/bin/bash
# the -x output goes to stderr, so to log it do:
set -x
exec 2 > /tmp/mylog

