mingw-get upgrade $(mingw-get list | awk '$1=="Package:" && $3=="Subsystem:" && NF==4{print $2}') 
