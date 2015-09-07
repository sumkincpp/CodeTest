#
# http://www.theperlreview.com/Articles/v0i1/one-liners.pdf
#
# The top 10 tricks of Perl one-liners (Ksplice Blog) 
# https://blogs.oracle.com/ksplice/entry/the_top_10_tricks_of
#
# command line - Perl flags -pe, -pi, -p, -w, -d, -i, -t? - Stack Overflow
# http://stackoverflow.com/questions/6302025/perl-flags-pe-pi-p-w-d-i-t
#
# perlrun - perldoc.perl.org
# http://perldoc.perl.org/perlrun.html
#
#
# -n similar to sed -n or awk
#  while (<>) {
#    ... # your program goes here
#  }
#
# -p flag ->
#  while (<>) {
#   # exec here 
#  } 
#  continue {
#    print or die "-p destination: $!\n"; 
#  }


# compare numbers with precision of 1%
perl -e 'sub cmpf { @_=sort(@_); abs(1 - $_[0]/$_[1]) > 0.01; } print cmpf(1.02, 1)."\n";'

# (WIN) unique folder name
ls | perl -ne "$s{$_}++||print"

# (WIN) unique lines from file
perl -ne "$s{$_}++||print" infile > outfile

# (WIN) grep an unique list of folders with a patter <1>-<WE WANT TO EXTRACT THIS>-<2>
ls | perl -ne " if ($_ =~ /- (.*?) -/ ) { $s{$1}++||print \"$1,\"; } "

# Base64 decode/encode perl oneliner
perl -MMIME::Base64 -e 'print encode_base64("string_to_encode")'
perl -MMIME::Base64 -e 'print decode_base64("string_to_decode")'


# Memory Leak
perl -e 'my @arr; while(1){ my @a = (1..1000000); push(@arr, \@a); }'
perl -e 'while(1){sub leak { my ($f, $b); $f = \$b; $b = \$f}; leak(); }'

# Simple replace - removing multiline comments 
perl -i.bak -pe 's/\/\*.*?\*\///' $file

# Substitution 
cat test | perl -pe 's/word/second/'
# remove trailing spaces in file
cat test | perl -pe 's/\s*$//'

# grep using perl text files (filter sorted)
ls | perl -nle 'print if -f && -T'

# Splitting like AWK PROFI
perl -F'\s+' -lane 'print $F[1];'
