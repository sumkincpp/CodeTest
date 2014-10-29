# cron sets LOGNAME user, other's is obvious
my $username = $ENV{LOGNAME} || $ENV{USER} || getpwuid($<);
