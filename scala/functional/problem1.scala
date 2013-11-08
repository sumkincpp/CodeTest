// Source :

val playerz = Map(1 -> Map("team" -> 1), 2 -> Map("team" -> 2), 3 -> Map("team" -> 1))

// Result :

val teamz: Map[Int, Seq[Int]) = Map(1 -> List(1, 3), 2 -> List(2))

// Solution :

playerz.groupBy(_._2("team")).mapValues(_.toList.map(_._1))

/*

scala> val playerz = Map(1 -> Map("team" -> 1), 2 -> Map("team" -> 2), 3 -> Map("team" -> 1))
playerz: scala.collection.immutable.Map[Int,scala.collection.immutable.Map[String,Int]] = Map(1 -> Map(team -> 1), 2 -> Map(team -> 2), 3 -> Map(team -> 1))

scala> playerz.groupBy(_._2("team")).mapValues(_.toList.map(_._1))
res0: scala.collection.immutable.Map[Int,List[Int]] = Map(2 -> List(2), 1 -> List(1, 3))

*/
