# Configuring tighvncserver 

Done on debian 7

   * `sudo apt-get install tightvncserver`
   * Configure /etc/init.d/vncservers
   * `update-rc.d vncserver defaults`
   * `service vncserver start`
   * `mkdir -p /etc/vncserver && vi /etc/vncserver/vncservers.conf`
   * Configure /etc/vncserver/vncservers.conf
