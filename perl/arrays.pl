
# Diff for array @a and @b -> getting every item from @a that doesn't exist in @b
# http://stackoverflow.com/questions/4891898/how-to-subtract-an-array-from-an-array
my %in_bl = map { $_ => 1 } @b;
my @diff  = grep { not $in_bl{$_} } @a;
