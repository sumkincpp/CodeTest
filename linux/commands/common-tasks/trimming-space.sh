$ echo "   lol  " | xargs
lol

$ echo "   test     test  " | xargs
test test

$ echo " test test " | tr -d ' '
testtest

$ echo " test test test " | sed -re 's/(^ *| *$)//'
test test test 
