```
C:\>net statistics server
Server Statistics for \\XXX


Statistics since 22.05.2017 14:48:02


Sessions accepted                  1
Sessions timed-out                 0
Sessions errored-out               2

Kilobytes sent                     1139
Kilobytes received                 1

Mean response time (msec)          0

System errors                      0
Permission violations              2
Password violations                0

Files accessed                     6
Communication devices accessed     0
Print jobs spooled                 0

Times buffers exhausted

  Big buffers                      0
  Request buffers                  0

The command completed successfully.



C:\>net statistics workstation
Workstation Statistics for \\XXX


Statistics since 22.05.2017 14:47:53


  Bytes received                               8511138
  Server Message Blocks (SMBs) received        94
  Bytes transmitted                            19460779
  Server Message Blocks (SMBs) transmitted     41
  Read operations                              15861
  Write operations                             0
  Raw reads denied                             0
  Raw writes denied                            0

  Network errors                               0
  Connections made                             3
  Reconnections made                           0
  Server disconnects                           6

  Sessions started                             0
  Hung sessions                                39
  Failed sessions                              0
  Failed operations                            0
  Use count                                    12887
  Failed use count                             9

The command completed successfully.


C:\>wmic os get lastbootuptime
LastBootUpTime
20170522144707.610798+180


Powershell :
Get-WinEvent -ProviderName eventlog | Where-Object {$_.Id -eq 6005 -or $_.Id -eq 6006}


C:\> systeminfo | find "System Boot Time:"
```
