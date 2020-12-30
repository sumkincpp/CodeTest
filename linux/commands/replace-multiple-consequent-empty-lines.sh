# replace-multiple-consequent-empty-lines.sh

cat -s
# -s --squeeze-blank: suppress repeated empty output lines.

perl -00pe0


sed 'N;/^\n$/D;P;D;'

# removes all empty lines
sed /^$/d 
