
# SERVER
# remove old & regenerate new

sudo /bin/rm -v /etc/ssh/ssh_host_*
sudo dpkg-reconfigure openssh-server

# CLIENT 
# remove host-key identification from clien machine

ssh-keygen -R server

