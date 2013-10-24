# Script snippet to check that provisioning was already done with "vagrant up"


if [ ! -f /vagrant/vagrant/installed ]; then
  #install LAMP 

  apt-get install -y apache2
  ....
  echo "done" >> /vagrant/vagrant/installed
fi
