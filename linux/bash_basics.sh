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
#
# Printing/Iterating WHOLE ARRAY
#
####################################################

ARR=(one two three)

echo ${ARR[@]}

####################################################
#
# Joining ARRAY WITH SEPARATOR
#
####################################################

function join { local IFS="$1"; shift; echo "$*"; }

ARR=(one two three)

RES=$(join "," ${ARR[@]})

echo $RES
# results on one,two,three

####################################################
#
# Logging in sys.out and file simultaniously
#
####################################################

program | tee pogram-0.log

####################################################

for i in {1..10}; do echo $i; done
