#!/usr/bin/perl
#-----------------------------------------------------------------------
# child.pl

use strict;
use warnings;

my ($user, $pw);

print("User:\n");
$user = <STDIN>;

print("Password:\n");
$pw = <STDIN>;

chomp($user);
chomp($pw);

print("Entered: $user/$pw\n");

# EOF
#-----------------------------------------------------------------------
