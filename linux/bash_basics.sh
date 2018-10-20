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

for i in `seq 1 10`; do echo $i; done 

####################################################

$ date "+%T %d %b %Y"
14:01:41 23 Apr 2014


####################################################
for f in `ls`; do
  echo "File -> $f"
done

####################################################
# Array 1
####################################################
farm_hosts=(web03 web04 web05 web06 web07)

for i in ${farm_hosts[@]}; do
  echo $i
done

####################################################
# Array 2
####################################################

## declare an array variable
declare -a arr=("element1" "element2" "element3")

## now loop through the above array
for i in "${arr[@]}"
do
   echo "$i"
   # or do whatever with individual element of the array
done

# You can access them using echo "${arr[0]}", "${arr[1]}" also
####################################################
