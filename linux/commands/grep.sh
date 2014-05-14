# grepping without filename (flag -h)
grep -h blabla .

# print only match
grep -o 'bla' .

# -I  - skip binaries, 
# --exclude-dir="\.svn"
grep -r --include=\*.{cpp,h} --exlclude="" piuu .
