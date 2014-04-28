R1#show ntp status
%NTP is not enabled.
R1#ping 193.93.167.241

Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 193.93.167.241, timeout is 2 seconds:
.!!!!
Success rate is 80 percent (4/5), round-trip min/avg/max = 64/84/112 ms
R1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#ntp server 193.93.167.241 prefer
R1#
Apr 28 06:14:04.749: %SYS-5-CONFIG_I: Configured from console by cisco on console
R1#show clock
06:14:13.410 UTC Mon Apr 28 2014
R1#show ntp status
Clock is synchronized, stratum 3, reference is 193.93.167.241
nominal freq is 250.0000 Hz, actual freq is 250.0000 Hz, precision is 2**18
reference time is D7087038.0BD13A2D (06:14:16.046 UTC Mon Apr 28 2014)
clock offset is 9.5981 msec, root delay is 76.40 msec
root dispersion is 29.57 msec, peer dispersion is 8.56 msec
R1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#clock timezone
% Incomplete command.

R1(config)#clock timezone MSK
% Incomplete command.

R1(config)#clock timezone MSK ?
  <-23 - 23>  Hours offset from UTC

R1(config)#clock timezone MSK 4
R1(config)#clock timezone MSK 4
Apr 28 06:16:21.601: %SYS-6-CLOCKUPDATE: System clock has been updated from 06:16:21 UTC Mon Apr 28 2014 to 10:16:21 MSK Mon Apr 28 2014, configured from console by cisco on console.
R1(config)#exit
R1#copy run start
Destination filename [startup-config]?
Building configuration...
[OK]

