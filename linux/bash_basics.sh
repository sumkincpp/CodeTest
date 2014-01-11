VAR="hello"
if [ -n "$VAR" ]; then
    echo "VAR is not empty"
fi

###############

VAR=""
if [ -z "$VAR" ]; then
    echo "VAR is empty"
fi
