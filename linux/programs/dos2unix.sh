# Just a snippet :D
grep -lIUr "^M" . | xargs sed -i 's/^M//'
