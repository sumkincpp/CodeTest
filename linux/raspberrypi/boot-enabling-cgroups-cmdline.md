# Raspberry PI - enabling cgroups

This will help cadvisor to show memory and CPU used ;)

- https://thesmarthomejourney.com/2022/08/01/fixing-cadvisor-cpu/
- https://askubuntu.com/questions/1189480/raspberry-pi-4-ubuntu-19-10-cannot-enable-cgroup-memory-at-boostrap
- https://forums.raspberrypi.com/viewtopic.php?t=383719

`cgroup_enable=cpuset cgroup_enable=memory cgroup_memory=1`

```
cat /boot/firmware/cmdline.txt
console=serial0,115200 cgroup_enable=cpuset cgroup_enable=memory cgroup_memory=1 console=tty1 root=PARTUUID=7a7d03cb-02 rootfstype=ext4 fsck.repair=yes rootwait fbcon=map:10 fbcon=font:VGA8x8 quiet splash plymouth.ignore-serial-consoles cfg80211.ieee80211_regdom=GE
```

Also `sudo rpi-update` is needed :/

- https://forums.raspberrypi.com/viewtopic.php?t=203128

```
cat /proc/cgroups
```
