#!/bin/env perl

use warnings;
use strict;

use Data::Dumper;

my $MYSQL_FOLDER='/var/lib/mysql/';
my $CONFIG_FILE="$MYSQL_FOLDER/my.cnf";
my $DB_USER='mysql';
my $DB_PASS='mysql';
my $DB_NAME='data';

sub query_db
{
  my $query=$_[0];

  my $cmd=`($MYSQL_FOLDER/bin/mysql --defaults-file=$CONFIG_FILE -N -B \\
     --user=$DB_USER \\
     --password=$DB_PASS \\
     $DB_NAME  \\
     -e "$query")`;

  return $cmd;# just a return trick!
}

print Dumper @ARGV;


print query_db($ARGV[0]);
