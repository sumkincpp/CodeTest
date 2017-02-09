curl -w '\nLookup:\t%{time_namelookup}\nConnect :\t%{time_connect}\nPreTrans:\t%{time_pretransfer}\nStartTeans:\t%{time_starttransfer}\n\nTotal time:\t%{time_total}\n' -o /dev/null -s https://www.google.com

curl -kso /dev/null -w "tcp:%{time_connect}, ssldone:%{time_appconnect}\n" https://www.google.com
