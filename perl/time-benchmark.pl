#!/usr/bin/env perl
#
# C:\Code\Code\perl>perl time-benchmark.pl
# 1.000057
#
use strict;
use warnings;

use Time::HiRes;
sub calc_time 
{
    my $func = shift;

    my $start_time = [Time::HiRes::gettimeofday()];
    $func->();
    my $elapsed_seconds = Time::HiRes::tv_interval($start_time);

    return $elapsed_seconds;
}


my $func = sub {
    sleep(1);
};

my $elapsed_secs = calc_time($func);

print($elapsed_secs);
