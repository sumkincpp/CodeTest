# substitutes charachters
tr [:upper:] [:lower:]
tr '[A-Z]' '[a-z]'

# deletes charachters
tr -d piu

# Squeze repeated chars
smt | tr -s ' ' | cut -d ' ' -f 4
# -s, --squeeze-repeats   replace each input sequence of a repeated character
#                         that is listed in SET1 with a single occurrence
#                         of that character
