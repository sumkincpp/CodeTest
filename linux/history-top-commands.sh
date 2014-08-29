awk '{print $1}' ~/.bash_history | sort | uniq -c | sort -n
