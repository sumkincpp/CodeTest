#
# Template for future common.sh library
#


# https://stackoverflow.com/a/9529981
function_exists() {
    declare -f -F $1 > /dev/null
    return $?
}
function_exists function_name && echo Exists || echo No such function
