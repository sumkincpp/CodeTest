[root@vagrant-centos65 ~]# groups
root

[root@vagrant-centos65 ~]# groups vagrant
vagrant : vagrant wheel

[root@vagrant-centos65 ~]# id -Gn vagrant
vagrant wheel

# Getting primary group
[root@vagrant-centos65 ~]# getent group vagrant
vagrant:x:500:

[root@vagrant-centos65 ~]# groupadd developers
[root@vagrant-centos65 ~]# usermod -a -G developers vagrant
[root@vagrant-centos65 ~]# groups vagrant
vagrant : vagrant wheel developers

# Changing primary group
[root@vagrant-centos65 ~]# usermod -g www tony

# Adding user
useradd -G admins,developers jerry

# Using `id`
[root@vagrant-centos65 ~]# id vagrant
uid=500(vagrant) gid=500(vagrant) groups=500(vagrant),10(wheel),502(developers)

[root@vagrant-centos65 ~]# id -G vagrant
500 10 502

[root@vagrant-centos65 ~]# id -Gn vagrant
vagrant wheel developers
