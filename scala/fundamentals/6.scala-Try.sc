
scala>  List(0,2).map { x => Try{ 1/x } }.map(_.map(_ + 2))
res127: List[scala.util.Try[Int]] = List(Failure(java.lang.ArithmeticException: / by zero), Success(2))

scala>  List(0,2).map { x => Try{ x*x/x } }.foreach(_.foreach(println(_)))
2
