sudo sed -i s/us.archive.ubuntu/old-releases.ubuntu/g /etc/apt/sources.list
sudo sed -i s/security.ubuntu/old-releases.ubuntu/g /etc/apt/sources.list
sudo apt-get update
