# Configuring tighvncserver 

Done on debian 7

   * `sudo apt-get install tightvncserver`
   * Configure /etc/init.d/vncservers
   * `update-rc.d vncserver defaults`
   * `mkdir -p /etc/vncserver && vi /etc/vncserver/vncservers.conf`
   * Configure /etc/vncserver/vncservers.conf
   * Configure /root/.vnc/xstartup to run X session (i.e. gnome-session)
   * `service vncserver start`

## Checking

`netstat -alpn | grep :5901` or `telnet localhost 5901`
