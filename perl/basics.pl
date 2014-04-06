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
