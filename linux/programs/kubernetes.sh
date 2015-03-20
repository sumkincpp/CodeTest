# kube services :D
ls /etc/init.d/ | grep kube | xargs -n1 -I% sudo service % stop
ls /etc/init.d/ | grep kube | xargs -n1 -I% sudo service % start
ls /etc/init.d/ | grep kube | xargs -n1 -I% sudo service % restart
