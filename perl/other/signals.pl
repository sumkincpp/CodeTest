#!/usr/bin/perl
use warnings;
use strict;

$SIG{__WARN__} = sub { die @_; };
$SIG{__DIE__} = sub { die @_; };

@ar = (1..3);

print "This should not be executed";
