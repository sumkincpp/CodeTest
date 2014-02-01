#!/usr/bin/expect
#
# sendswitchcmd.sh
#
#     ./sendswitchcmd.exp [switch-IP] "show vlans"
#
# http://stackoverflow.com/questions/21436585/using-perl-and-openssh-to-interact-with-a-switch
#
set timeout 60

spawn ssh -t -t -o ConnectTimeout=5 -o StrictHostKeyChecking=no -i PATHTOYOURKEY]
expect -re "Press any key to continue"
send "X"
expect -re ".*#"
send "config\n"
expect -re ".*#"
send "[lindex $argv 1] [lindex $argv 2]\n     "
expect -re ".*#"
send "ex\n"
expect -re ".*#"
send "ex\n"
expect -re ".*>"
send "ex\n"
expect -re ".*you want to log out.*"
send "y"
