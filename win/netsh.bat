C:\Program Files\Far Manager>netsh interface ip show interfaces

Idx     Met         MTU          State                Name
---  ----------  ----------  ------------  ---------------------------
  1          50  4294967295  connected     Loopback Pseudo-Interface 1
 10          20        1300  connected     Local Area Connection
 12          10        1300  disconnected  Local Area Connection 2
 14          20        1300  connected     VirtualBox Host-Only Network
 26          20        1500  connected     VMware Network Adapter VMnet1
 27          20        1500  connected     VMware Network Adapter VMnet8
 23           1        1210  connected     Local Area Connection 3
 17          20        1300  connected     VirtualBox Host-Only Network #2
 
C:\Code>netsh interface show interface

Admin State    State          Type             Interface Name
-------------------------------------------------------------------------
Enabled        Connected      Dedicated        Local Area Connection
Enabled        Disconnected   Dedicated        Local Area Connection 2
Enabled        Connected      Dedicated        VMware Network Adapter VMnet1
Enabled        Connected      Dedicated        VMware Network Adapter VMnet8
Enabled        Connected      Dedicated        VirtualBox Host-Only Network
Disabled       Disconnected   Dedicated        Cisco AnyConnect Secure Mobility Client Connection
Enabled        Connected      Dedicated        VirtualBox Host-Only Network #2

rem ----------------------------------------
netsh firewall show state
netsh firewall show opmode
netsh firewall show port
netsh firewall show config

netsh firewall set portopening protocol = TCP port = 1434 name = SQLPort mode = ENABLE scope = SUBNET profile = CURRENT
