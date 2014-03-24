# Removing exact element from array

my @array = (1,2,3,4,5,5,6,5,4,9);
my $element_omitted = 5;
@array = grep { $_ != $element_omitted } @array;

my $index = 0;
$index++ until $arr[$index] eq 'foo';
splice(@arr, $index, 1);
