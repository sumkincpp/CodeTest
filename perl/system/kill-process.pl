#!/usr/bin/env sh
# $$ -- The process number of the Perl running this script. 

#
# If pid is negative, but not -1, sig shall be sent to all processes 
# (excluding an unspecified set of system processes) whose process 
# group ID is equal to the absolute value of pid, and for which 
# the process has permission to send a signal.
#

#
# The spec says to all processes within the given group. 
# There can be multiple processes per group. 
# The negative id identifies the group
#
# SUSv4
# http://pubs.opengroup.org/onlinepubs/9699919799/functions/kill.html
#


{
  local $SIG{TERM} = "IGNORE"; # ignoring actual kill
  
  kill TERM, $$; # kill 9, $$;
}
