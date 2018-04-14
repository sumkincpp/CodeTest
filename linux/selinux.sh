ls -Z
restorecon -r -vF /var/

getenforce
sestatus

grep "SELinux is preventing" /var/log/messages

touch /.autorelabel; reboot
