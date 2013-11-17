
#unique file (not a pipe version!!)
ruby -e "puts IO.readlines(ARGV[0]).uniq" infile > outfile

