#!/usr/bin/env perl
#
# In Perl, how can I read an entire file into a string?
# http://stackoverflow.com/questions/953707/in-perl-how-can-i-read-an-entire-file-into-a-string
#

sub get_file_contents 
{
  local $/ = undef; # It's a slurp mode, so we rea not by line, but whole file
  open my $fh, "<", $_[0] 
      or die "could not open $file: $!";
  my $res = <$fh>;
  close $fh;  
}

# also,
# Closing filehandles is not neccesary http://www.perlmonks.org/?node_id=902128 

print get_file_contents("hello.txt");
