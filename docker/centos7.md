# Installing obsolete 17.03.2

I.e. due to package renaming, it can't be installed :
```bash
[root@k8s-master ~]# yum install docker-ce-17.03.2.ce-1.el7.centos docker-ce-selinux-17.03.2.ce-1.el7.centos.noarch
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
 * base: mirror.yandex.ru
 * extras: mirror.yandex.ru
 * updates: mirror.yandex.ru
Package docker-ce-selinux is obsoleted by docker-ce, trying to install docker-ce-18.03.1.ce-1.el7.centos.x86_64 instead
Resolving Dependencies
--> Running transaction check
---> Package docker-ce.x86_64 0:17.03.2.ce-1.el7.centos will be installed
--> Processing Dependency: docker-ce-selinux >= 17.03.2.ce-1.el7.centos for package: docker-ce-17.03.2.ce-1.el7.centos.x86_64
Package docker-ce-selinux is obsoleted by docker-ce, but obsoleting package does not provide for requirements
---> Package docker-ce.x86_64 0:18.03.1.ce-1.el7.centos will be installed
--> Processing Dependency: container-selinux >= 2.9 for package: docker-ce-18.03.1.ce-1.el7.centos.x86_64
--> Running transaction check
---> Package container-selinux.noarch 2:2.55-1.el7 will be installed
---> Package docker-ce.x86_64 0:17.03.2.ce-1.el7.centos will be installed
--> Processing Dependency: docker-ce-selinux >= 17.03.2.ce-1.el7.centos for package: docker-ce-17.03.2.ce-1.el7.centos.x86_64
Package docker-ce-selinux is obsoleted by docker-ce, but obsoleting package does not provide for requirements
--> Finished Dependency Resolution
Error: Package: docker-ce-17.03.2.ce-1.el7.centos.x86_64 (docker-ce-stable)
           Requires: docker-ce-selinux >= 17.03.2.ce-1.el7.centos
           Available: docker-ce-selinux-17.03.0.ce-1.el7.centos.noarch (docker-ce-stable)
               docker-ce-selinux = 17.03.0.ce-1.el7.centos
           Available: docker-ce-selinux-17.03.1.ce-1.el7.centos.noarch (docker-ce-stable)
               docker-ce-selinux = 17.03.1.ce-1.el7.centos
           Available: docker-ce-selinux-17.03.2.ce-1.el7.centos.noarch (docker-ce-stable)
               docker-ce-selinux = 17.03.2.ce-1.el7.centos
 You could try using --skip-broken to work around the problem
 You could try running: rpm -Va --nofiles --nodigest
```

But this will work :
```bash
yum install --setopt=obsoletes=0 \
   docker-ce-17.03.2.ce-1.el7.centos.x86_64 \
   docker-ce-selinux-17.03.2.ce-1.el7.centos.noarch
```
