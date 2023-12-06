# timedatectl

```bash
$ timedatectl
               Local time: Wed 2023-12-06 12:32:58 UTC
           Universal time: Wed 2023-12-06 12:32:58 UTC
                 RTC time: Wed 2023-12-06 12:32:56
                Time zone: Etc/UTC (UTC, +0000)
System clock synchronized: no
              NTP service: inactive
          RTC in local TZ: no
$ sudo timedatectl set-timezone Europe/Berlin
$ timedatectl
               Local time: Wed 2023-12-06 13:34:53 CET
           Universal time: Wed 2023-12-06 12:34:53 UTC
                 RTC time: Wed 2023-12-06 12:34:52
                Time zone: Europe/Berlin (CET, +0100)
System clock synchronized: no
              NTP service: inactive
          RTC in local TZ: no

```
