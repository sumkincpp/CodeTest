#!/bin/bash
# duct taped by one.time
# Basic interface information collector

##
# Set usage var and getoptions
usage="Usage: interface-info.sh -H <IP Address> -C <snmp community string>

OPTIONS:
  -H Hostname          set IP address or hostname
  -h Help              prints usage options

SNMPv2 OPTIONS:
  -C Community         set SNMPv2 community string
"

while getopts H:C:h option;
do
        case $option in
                H) ipaddress=$OPTARG;;
                C) community=$OPTARG;;
                h) echo "$usage"
                exit $invalid_result;;
        esac
done

##
# Prevent blank argvars
if [[ -z $ipaddress || -z $community ]]; then
  echo "$usage"
  exit 0
fi

## 
# Set field separator to new line
IFS=$'\n'

##
# Store our IP-MIB info in arrays
ipAdEntAddr=( $(snmpbulkwalk -v2c -c $community  $ipaddress .1.3.6.1.2.1.4.20.1.1 | awk -F ": " '{print $2}') )
ipAdEntNetMask=( $(snmpbulkwalk -v2c -c $community $ipaddress .1.3.6.1.2.1.4.20.1.3 | awk -F ": " '{print $2}') )
ipAdEntIfIndex=( $(snmpbulkwalk -v2c -c $community $ipaddress .1.3.6.1.2.1.4.20.1.2 | awk -F ": " '{print $2}') )

for ((i=0; i<${#ipAdEntAddr[@]}; i++)); do
  ifDescr[$i]=$(snmpwalk -v2c -c $community $ipaddress .1.3.6.1.2.1.2.2.1.2.${ipAdEntIfIndex[$i]} | awk -F ": " '{print $2}')
  echo "${ifDescr[$i]}: ${ipAdEntAddr[$i]} ${ipAdEntNetMask[$i]}"
done
