#!/usr/bin/env perl

use strict;
use warnings;

use JSON;

#my $json = JSON->new;
my $json = JSON->new->utf8;

my $data = do { local $/; <DATA> };
my $hash = decode_json $data;

print $json->pretty->encode($hash);

__DATA__
{"glossary":{"title":"example glossary","GlossDiv":{"title":"S","GlossList":
{"GlossEntry":{"ID":"SGML","SortAs":"SGML","GlossTerm":"Standard Generalized Markup Language",
"Acronym":"SGML","Abbrev":"ISO 8879:1986","GlossDef":{"para":
"A meta-markup language,used to create markup languages such as DocBook.",
"GlossSeeAlso":["GML","XML"]},"GlossSee":"markup"}}}}}
