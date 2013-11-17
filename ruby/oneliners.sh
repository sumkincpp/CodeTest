# unique file (not a pipe version!!)
ruby -e "puts IO.readlines(ARGV[0]).uniq" infile > outfile

# (WIN) Inplace replace of 'hello' to 'hello world' with creation of .bak file
# (LINUX) Remove .bak and no backup file will be created
ruby -i.bak -pe "gsub('hello', 'hello world')" test.txt
