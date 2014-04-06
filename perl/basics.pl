#!/usr/bin/perl -w


# HEREDOC -------------------------------------------

my $heredoc = <<END;
THIS IS A MULTILINE 
HEREDOC
END

print $heredoc; 

# <DATA> -------------------------------------------

my $data = do { local $/; <DATA> };

print $data;

__DATA__

SOME data with #$%^&*( symbols, also tags
and bla bla bla


# ClearScreen -----------------------------------------

print "\033[2J";   #clear the screen
print "\033[0;0H"; #jump to 0,0

