####################################################
#
# Checking if bash variable is empty or not
#
####################################################

VAR="hello"
if [ -n "$VAR" ]; then
    echo "VAR is not empty"
fi

####################################################

VAR=""
if [ -z "$VAR" ]; then
    echo "VAR is empty"
fi

####################################################
#
# Listing files in folder
#
####################################################

# Mistaken approach as every " " counts as separator :

for i in `ls /opt/Docs`; do echo $i; done;

# Proper approach, one file - one line :

ls /opt/Docs | while read i; do echo $i; done;


####################################################
