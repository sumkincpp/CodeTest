# vagrant boxes
```
vagrant box update --box centos/7
```

# vagrant plugin

```
vagrant plugin install vagrant-vbguest
```

```
$ sudo apt-get install linux-headers-`uname -r` build-essentials
$ sudo blkid | grep VBox
/dev/sr0: BLOCK_SIZE="2048" UUID="2024-05-02-09-22-15-23" LABEL="VBox_GAs_7.0.18" TYPE="iso9660"
$ sudo mkdir /media/cdrom/
$ sudo mount /dev/sr0 /media/cdrom/
$ sudo /media/cdrom/VBoxLinuxAdditions.run
```

```
$ sudo /media/cdrom/VBoxLinuxAdditions.run
Verifying archive integrity...  100%   MD5 checksums are OK. All good.
Uncompressing VirtualBox 7.0.18 Guest Additions for Linux  100%
VirtualBox Guest Additions installer
Removing installed version 7.0.18 of VirtualBox Guest Additions...
Copying additional installer modules ...
Installing additional modules ...
VirtualBox Guest Additions: Starting.
VirtualBox Guest Additions: Setting up modules
VirtualBox Guest Additions: Building the VirtualBox Guest Additions kernel
modules.  This may take a while.
VirtualBox Guest Additions: To build modules for other installed kernels, run
VirtualBox Guest Additions:   /sbin/rcvboxadd quicksetup <version>
VirtualBox Guest Additions: or
VirtualBox Guest Additions:   /sbin/rcvboxadd quicksetup all
VirtualBox Guest Additions: Building the modules for kernel 5.15.0-117-generic.
update-initramfs: Generating /boot/initrd.img-5.15.0-117-generic
VirtualBox Guest Additions: Running kernel modules will not be replaced until
the system is restarted or 'rcvboxadd reload' triggered
VirtualBox Guest Additions: reloading kernel modules and services
VirtualBox Guest Additions: kernel modules and services 7.0.18 r162988 reloaded
VirtualBox Guest Additions: NOTE: you may still consider to re-login if some
user session specific services (Shared Clipboard, Drag and Drop, Seamless or
Guest Screen Resize) were not restarted automatically

```