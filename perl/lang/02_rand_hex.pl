
my $rand_hex = join "", map { unpack "H*", chr(rand(256)) } 1..16;
