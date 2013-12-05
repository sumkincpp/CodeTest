#!/usr/local/bin/perl
# Simple regex for price matching
use strict;
use warnings;

while (<DATA>) {
  print "(matched) " if /^\$ (([1-9][0-9]{0,2}(,[0-9]{3})*|[0-9])\.([0-9]{2}))?$/;
  print $_. "\n";
}


__DATA__
# Should be matched

$ 214,190,133,233.00
$ 190,133,233.00
$ 122,224.00
$ 20,323.43
$ 5,825.90
$ 0.00

# Unmatched

$ 12
$ 50,34,4
$ 5453,43
$ 32,00
$ 0,444.44
$ 576.667
$ 0,855,678.88
