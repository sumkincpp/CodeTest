
ps -C "qemu-system-x86" -L -o pid,lwp,pcpu,cpuid,time,args | sort -nrk 3 | cut -c -150 | head -30; numactl -H; free -m 
