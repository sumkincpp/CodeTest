[root@vagrant-centos65 ~]# groups
root

[root@vagrant-centos65 ~]# groups vagrant
vagrant : vagrant wheel

[root@vagrant-centos65 ~]# id -Gn vagrant
vagrant wheel

# Getting primary group
[root@vagrant-centos65 ~]# getent group vagrant
vagrant:x:500:
