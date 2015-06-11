#!/usr/bin/perl
# https://stackoverflow.com/questions/11514947/capture-the-output-of-perl-system

use strict;
use warnings;

open CMD,'-|','commandddd' or die $@;
my $line;
while (defined($line=<CMD>)) {
    print $line; #or push @table,$line or do whatewer what you want processing line by line
}
close CMD;
