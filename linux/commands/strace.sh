strace -s10000 -feprocess -o strace.txt ./piuuu

strace -s10000 -f -e verbose=all -e trace=execve -v -p 5287
