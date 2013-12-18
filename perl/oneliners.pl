#
# http://www.theperlreview.com/Articles/v0i1/one-liners.pdf
#

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
