#!/bin/perl

# more nice converters > http://aerostitch.github.io/programming/perl/oneliners/perl_numbers_conversion.html

foreach my $arg (@ARGV) {
	my ($decimal, $binary) = ($arg, '');

	$SIG{USR1} = sub { $binary .= "0"};
	$SIG{USR2} = sub { $binary .= "1"};

	do { kill $decimal & 1 ? 'USR2' : 'USR1' , $$;
		 $decimal >>= 1;
	} while ($decimal);

	print $arg. " = ". scalar reverse $binary;
	print "\n";
}
