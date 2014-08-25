# Scala 2.8
scala> val listOfOptions = List(None, Some("hi"), None)
listOfOptions: List[Option[java.lang.String]] = List(None, Some(hi), None)

scala> listOfOptions flatten
res0: List[java.lang.String] = List(hi)
