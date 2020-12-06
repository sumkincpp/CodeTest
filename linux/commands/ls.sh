# classify (-F) and get only files from folder
# note: binaries would be marked*
ls -F | grep -v '/'

# -p --- append / indicator to directories
ls -p | grep -v '/'


# list line by line
ls -1a