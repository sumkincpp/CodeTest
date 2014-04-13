# So you don't get bitten again, find out what version of tcl you have
# ([info patchlevel]), and make sure you have a link to the appropriate
# docs (http://www.tcl.tk/man)

# If it's not built-in, you have to build it yourself.

proc pow {x y} {
  expr {$y == 0 ? 1 : $x * [pow $x [incr y -1]]}
}
