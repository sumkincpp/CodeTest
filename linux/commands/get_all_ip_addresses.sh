
# First variant
/sbin/ifconfig | perl -nle'/dr:(\S+)/ && print $1'

# Second variant
/sbin/ifconfig | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}'
