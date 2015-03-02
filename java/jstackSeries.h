#!/bin/bash
#
# https://helpx.adobe.com/experience-manager/kb/TakeThreadDump.html
# http://wiki.eclipse.org/How_to_report_a_deadlock#jstackSeries_--_jstack_sampling_in_fixed_time_intervals_.28tested_on_Linux.29
#
if [ $# -eq 0 ]; then
    echo >&2 "Usage: jstackSeries [ [ ] ]"
    echo >&2 " Defaults: count = 10, delay = 0.5 (seconds)"
    exit 1
fi
pid=$1 # required
user=$2 # required
count=${3:-10} # defaults to 10 times
delay=${4:-0.5} # defaults to 0.5 seconds
while [ $count -gt 0 ]
do
    sudo -u $user jstack -l $pid >jstack.$pid.$(date +%H%M%S.%N)
    sleep $delay
    let count--
    echo -n "."
done
