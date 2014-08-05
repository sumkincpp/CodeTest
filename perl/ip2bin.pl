#!/usr/bin/perl

print ip2bin($ARGV[0], ".")

sub ip2bin
{
    my ($ip, $delimiter) = @_;
    return     join($delimiter,  map 
        substr(unpack("B32",pack("N",$_)),-8), 
        split(/\./,$ip));
}
