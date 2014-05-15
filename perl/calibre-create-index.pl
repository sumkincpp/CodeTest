#!/usr/bin/env perl

use strict;
use warnings;


my @dirs = split /\n/, `find . -type d`;

# @dirs = map { $_ =~ s%(.\/?)%%; $_ } @dirs;

my $data = do { local $/; <DATA> };

my $res = '';

foreach my $dir (@dirs) {
	#print $dir. " \n";

	# 2>/dev/null to suppress error bullshit
	my @files = split /\n/, `ls $dir/*.html 2>/dev/null`;



	foreach my $file (@files) {
		my $name = $file;
		$file =~ s%(.\/?)%%;

		#if ($name =~ /(.*)\/(.*)\.html/) {
	#		my $folder = $1;
#			$folder =~ s%/%%;
#			print $2;
			# body...
#		}
		$name =~ s%(.\/?)%%;
		$res .= "      <a href='$file'>$name</a><br/>\n";
	}
}

$data =~ s%__CONTENTS__%$res%;

print $data;

__DATA__

<html>
   <body>
     <h1>Table of Contents</h1>
     <p style="text-indent:0pt">
     	__CONTENTS__
     </p>
   </body>
</html>
