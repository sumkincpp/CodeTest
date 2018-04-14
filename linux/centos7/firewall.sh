
sudo firewall-cmd --get-zones
sudo firewall-cmd --list-all-zones
sudo firewall-cmd --get-active-zones
sudo firewall-cmd --get-services

sudo firewall-cmd --zone=public --list-services

# Logging denieds packets - /var/log/messages
sudo firewall-cmd --set-log-denied=all

# Adding service
sudo firewall-cmd --add-service=dhcp --permanent

# Opening port :
sudo firewall-cmd --zone=dmz --add-port=2888/tcp --permanent

sudo firewall-cmd --reload


