

# -w0 flag tells ioreg not to truncate the output lines, and the 
# -l flag is the list command, which is what actually generates the output.

ioreg -l | grep "Cycle Count"
ioreg -l | grep Capacity
ioreg -c AppleSmartBattery | grep -i Capacity  # same as above
ioreg -w0 -l | grep Capacity # same
ioreg -rn AppleSmartBattery # more concrete output

#----------------------------------------
# Current Battery wear factor
ioreg -n AppleSmartBattery | \
    awk '/MaxCapacity/{ MAX=$5 }
         /CurrentCapacity/{ CURRENT=$5 }
         /InstantTimeToEmpty/{ REMAIN=$5 }
    END { printf("%5.2f%% %2dh%2dm\n", CURRENT/MAX*100, REMAIN/60, REMAIN%60) }'
    
#----------------------------------------
# Other helpers(though it's really easy to write them) :
# https://rustyisageek.blogspot.ru/2010/03/monitoring-battery-status-through.html

#Cycle Count
ioreg -l | grep Capacity | grep "Cycle Count"| cut -d, -f6 |sed -e s/\"//g | sed -e s/}//g
#Cycle Count Number Only
ioreg -l | grep Capacity | grep "Cycle Count"| cut -d, -f6 |sed -e s/\"Cycle\ Count\"=//g | sed -e s/}//g
#Max Capacity
ioreg -l | grep MaxCapacity | sed s/\"//g| awk '{print $3,$4,$5}'
#Max Capacity Number Only
ioreg -l | grep MaxCapacity | sed s/\"//g | awk '{print $5}'
#Current Capacity
ioreg -l | grep CurrentCapacity | sed s/\"//g| awk '{print $3,$4,$5}'
#Current Capacity Number Only
ioreg -l | grep CurrentCapacity | sed s/\"//g | awk '{print $5}'
##Design Capacity
ioreg -l | grep DesignCapacity | sed s/\"//g | awk '{print $3,$4,$5}'
#Design Capacity Number Only
ioreg -l | grep DesignCapacity | sed s/\"//g | awk '{print $5}'
