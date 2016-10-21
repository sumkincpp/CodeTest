#!/usr/bin/env perl
use strict;
use warnings;

# We will allow loading Package files from the same folder 
# So, it will be possible to run script relatively to some other folder, i.e. blah/meh/blah/script_bootstrap_1.pl
# And package still will be found (i.e. because, ordinarily, only "." folder is added)
use File::Basename;
use lib dirname(__FILE__);

use XXXPackage;
