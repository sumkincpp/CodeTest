## Should be run in REPL mode

scala> implicit class Test(row:String) { def foo = println(row) }
defined class Test

scala> List("fgs", "fds").map(_.foo)
fgs
fds
res0: List[Unit] = List((), ())

scala> "fdsfds".foo
fdsfds
