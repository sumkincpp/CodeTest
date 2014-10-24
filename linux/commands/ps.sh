# Showing PID, Parent PID, Procees Group ID (j flag)
$ ps laj
  UID   PID  PPID CPU PRI NI      VSZ    RSS WCHAN  STAT   TT       TIME COMMAND          USER   PGID   SESS JOBC
  501 71733   643   0  31  0  2461332   1436 -      Ss+  s003    0:00.41 -/usr/local/bin/ fedor 71733      0    0
  501 71802   643   0  31  0  2461328   1092 -      Ss+  s010    0:00.36 -/usr/local/bin/ fedor 71802      0    0
  501 15405   643   0  31  0  2453028   3748 -      Ss   s011    0:00.09 -/bin/bash       fedor 15405      0    0
    0 15454 15405   0  31  0  2432800    724 -      R+   s011    0:00.00 ps laj           root  15454      0    1

# Sort by memory +human readable
$ ps -eo size,pid,user,command --sort -size | awk '{ hr=$1/1024 ; printf("%13.2f Mb ",hr) } { for ( x=4 ; x<=NF ; x++ ) { printf("%s ",$x) } print "" }' | tail
  0.00 Mb [ext4-dio-unwrit]
  0.00 Mb [kauditd]
  0.00 Mb [vmmemctl]
  0.00 Mb [jbd2/sda1-8]
  0.00 Mb [ext4-dio-unwrit]
  0.00 Mb [ext4-dio-unwrit]
  0.00 Mb [flush-253:0]
  0.00 Mb [rpciod/0]
  0.00 Mb [rpciod/1]
  0.00 Mb [sm_elasticsearc] <defunct>

# Total memory usage for java (for example) processes
$ ps -C java -O rss | gawk '{ count ++; sum += $2 }; END {count --; print "Number of processes =",count; print "Memory usage per process =",sum/1024/count, "MB"; print "Total memory usage =", sum/1024, "MB" ;};'
Number of processes = 23
Memory usage per process = 326.818 MB
Total memory usage = 7516.8 MB
