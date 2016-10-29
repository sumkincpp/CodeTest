#!/usr/bin/perl

use 5.18.2;
use warnings;

use HTML::TreeBuilder;

my $root = HTML::TreeBuilder->new_from_file (\*DATA);

$root->look_down (_tag => "div", id => "footer")
    ->replace_with (HTML::Element->new ("~comment", text => " foobar "
+));

say $root->as_HTML (undef, "  ", {});

__DATA__
<div id="quiteok">ok</div>
<div id="footer">
 bad
 <div>
  stuff
  <div>
   and lots of it
  </div>
 </div>
</div>
<div>
 something good
</div>
