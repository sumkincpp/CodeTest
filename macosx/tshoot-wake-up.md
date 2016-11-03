
Wake up assertions :
```sh
pmset -g assertions
```
Check reasons for wake up in syslog
```sh
syslog | grep -i "Wake reason"
```
Or even
```sh
syslog -k Sender kernel -k Message Req Wake
```


 * OHC: stands for Open Host Controller, is usually USB or Firewire. If you see OHC1 or OHC2 it is almost certainly an external USB keyboard or mouse that has woken up the machine.
 * EHC: standing for Enhanced Host Controller, is another USB interface, but can also be wireless devices and bluetooth since they are also on the USB bus of a Mac.
 * USB: a USB device woke the machine up
 * LID0: this is literally the lid of your MacBook or MacBook Pro, when you open the lid the machine wakes up from sleep.
 * PWRB: PWRB stands for Power Button, which is the physical power button on your Mac
 * RTC: Real Time Clock Alarm, is generally from wake-on-demand services like when you schedule sleep and wake on a Mac via the Energy Saver control panel. It can also be from launchd setting, user applications, backups, and other scheduled events.
