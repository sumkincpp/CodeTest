# grabbed somewhere from SO
history | awk '{h[$2]++}END{for(i in h){print h[i],i|"sort -rn|head -20"}}' |awk '!max{max=$1;}{r="";i=s=60*$1/max;while(i-->0)r=r"#";printf "%15s %5d %s %s",$2,$1,r,"\n";}'
