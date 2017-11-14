# find all files with ':' in naming and remove that damn sign
find . | grep -a '[:?]' | tr '\n' '\0' | xargs -0 -n1 -I%% sh -c "mv '%%' \$(echo '%%' | tr -d ':?')"
