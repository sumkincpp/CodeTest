
#
# http://www.perlmonks.org/?node_id=406883
#

# max 
my $max = ($x, $y)[$x < $y]; 

# min 
my $min = ($x, $y)[$x > $y];

sub max ($$) { $_[$_[0] < $_[1]] } 
sub min ($$) { $_[$_[0] > $_[1]] } 
