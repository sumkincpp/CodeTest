# Showing PID, Parent PID, Procees Group ID (j flag)
$ ps laj
  UID   PID  PPID CPU PRI NI      VSZ    RSS WCHAN  STAT   TT       TIME COMMAND          USER   PGID   SESS JOBC
  501 71733   643   0  31  0  2461332   1436 -      Ss+  s003    0:00.41 -/usr/local/bin/ fedor 71733      0    0
  501 71802   643   0  31  0  2461328   1092 -      Ss+  s010    0:00.36 -/usr/local/bin/ fedor 71802      0    0
  501 15405   643   0  31  0  2453028   3748 -      Ss   s011    0:00.09 -/bin/bash       fedor 15405      0    0
    0 15454 15405   0  31  0  2432800    724 -      R+   s011    0:00.00 ps laj           root  15454      0    1
