
## Usage

```
# sysdig -cl

Category: CPU Usage
-------------------
spectrogram         Visualize OS latency in real time.
subsecoffset        Visualize subsecond offset execution time.
topcontainers_cpu   Top containers by CPU usage
topprocs_cpu        Top processes by CPU usage

Category: Errors
----------------
topcontainers_error Top containers by number of errors
topfiles_errors     Top files by number of errors
topprocs_errors     top processes by number of errors

Category: I/O
-------------
echo_fds            Print the data read and written by processes.
fdbytes_by          I/O bytes, aggregated by an arbitrary filter field
fdcount_by          FD count, aggregated by an arbitrary filter field
fdtime_by           FD time group by
iobytes             Sum of I/O bytes on any type of FD
iobytes_file        Sum of file I/O bytes
spy_file            Echo any read/write made by any process to all files. Optio
                    nally, you can provide the name of one file to only interce
                    pt reads/writes to that file.
stderr              Print stderr of processes
stdin               Print stdin of processes
stdout              Print stdout of processes
topcontainers_file  Top containers by R+W disk bytes
topfiles_bytes      Top files by R+W bytes
topfiles_time       Top files by time
topprocs_file       Top processes by R+W disk bytes

Category: Logs
--------------
spy_logs            Echo any write made by any process to a log file. Optionall
                    y, export the events around each log message to file.
spy_syslog          Print every message written to syslog. Optionally, export t
                    he events around each syslog message to file.

Category: Misc
--------------
around              Export to file the events around the where the given filter
                     matches.

Category: Net
-------------
iobytes_net         Show total network I/O bytes
spy_ip              Show the data exchanged with the given IP address
spy_port            Show the data exchanged using the given IP port number
topconns            Top network connections by total bytes
topcontainers_net   Top containers by network I/O
topports_server     Top TCP/UDP server ports by R+W bytes
topprocs_net        Top processes by network I/O

Category: Performance
---------------------
bottlenecks         Slowest system calls
fileslower          Trace slow file I/O
netlower            Trace slow network I/0
proc_exec_time      Show process execution time
scallslower         Trace slow syscalls
topscalls           Top system calls by number of calls
topscalls_time      Top system calls by time

Category: Security
------------------
list_login_shells   List the login shell IDs
shellshock_detect   print shellshock attacks
spy_users           Display interactive user activity

Category: System State
----------------------
lscontainers        List the running containers
lsof                List (and optionally filter) the open file descriptors.
netstat             List (and optionally filter) network connections.
ps                  List (and optionally filter) the machine processes.

Use the -i flag to get detailed information about a specific chisel
```

## Writing
```
sysdig -w trace.scap
sysdig -zw trace.scap.gz
sysdig -zw trace.scap.gz-s 4096
```

## Live
```
# sysdig -p "%proc.name %fd.name" "evt.type=accept and pc.name!=httpd" | head
java 127.0.0.1:54991->127.0.0.1:58080
java 127.0.0.1:54992->127.0.0.1:58080
java 127.0.0.1:54993->127.0.0.1:58080
java 127.0.0.1:54994->127.0.0.1:58080
java 127.0.0.1:54995->127.0.0.1:58080
java 127.0.0.1:54996->127.0.0.1:58080
java 127.0.0.1:54997->127.0.0.1:58080
java 127.0.0.1:54998->127.0.0.1:58080
java 127.0.0.1:54999->127.0.0.1:58080
java 127.0.0.1:55000->127.0.0.1:58080
```

```
# sysdig -c topprocs_net
Bytes           Process         PID
--------------------------------------------------------------------------------
368B            sshd            25833
```

```
sysdig -pc -c topcontainers_net
```

## Read

```
sudo sysdig -r trace.scap.gz -c topprocs_net
```
