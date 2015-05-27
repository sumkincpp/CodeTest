# from expect package
unbuffer long_running_command | print_progress

# Immediate unbuffering
stdbuf -i0 -o0 -e0 command

# Line unbuffering
stdbuf -oL -eL command

script -q /dev/null long_running_command | print_progress      # FreeBSD, Mac OS X
script -c "long_running_command" /dev/null | print_progress    # Linux

grep --line-buffered

sed -u
