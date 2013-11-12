Hi!

I'm new using Scala and Play2 and yesterday I found the string interpolation method to format a String in this link
and I noticed the possibility of implementing a custom definition. Then, when I was writing a new Anorm SQL query I realized this could be a good experiment. The advantage of using string interpolation is that it's more concise and easier to read. Let's see an example:

    SQL("select * from car where brand = {brand} and color = {color} and year = {year} order by name").on("brand" -> brand, "color" -> color, "year" -> year).as(Car.simple *)

It's only a simple example, but imagine it with more parameters. It wouldn't be better something like that?

    SQL"select * from car where brand = $brand and color = $color and year = $year order by name".as(Car.simple *)

Here, the syntaxis is more concise, and every parameter value is next to its name so it's also clearer.

I think it would be nice to get this functionality for next versions of Play, but for now I have implemented the code below. My intention is to share this tip and if anybody knows how to improve it, please do it. I'm a newbe in scala and the algorithm is very simple but probably it could be more efficient (maybe using iterators instead of zip function for getting the query).

```
object AnormHelpers {

  implicit class AnormHelper (val sc: StringContext) extends AnyVal {
    def SQL (args: Any*) = {
      // Matches every argument to an arbitrary name -> ("p0", value0), ("p1", value1), …
      val params = args.zipWithIndex.map(p => ("p"+p._2, p._1))
      // Regenerates the original query substituting each argument by its name -> "select * from car where id = {p0}"
      val query = (sc.parts zip params).map{ case (s, p) => s + "{"+p._1+"}" }.mkString("") + sc.parts.last
      // Creates the anorm.Sql
      anorm.SQL(query).on( params.map(p => (p._1, anorm.toParameterValue(p._2))) :_*)
    }
  }

}
```

In addition, it's also possible to customize a bit more to trim and eliminates multiple spaces in any String value (don't use for passwords, for example):

```
def SQLt (args: Any*) = {
  val params = args.zipWithIndex.map {
    case (arg: String, index) => ("p"+index, arg.trim.replaceAll("\\s{2,}", " "))
    case (arg, index) => ("p"+index, arg)
  }
  val query = (sc.parts zip params).map{ case (s, p) => s + "{"+p._1+"}" }.mkString("") + sc.parts.last
  anorm.SQL(query).on( params.map(p => (p._1, anorm.toParameterValue(p._2))) :_*)
}
```

And even more, for example, to support the IN clause:

```
def SQLin (args: Any*) = {
  // Matches every argument to an arbitrary name -> ("p0", value0), ("p1", value1), ...
  val params = args.zipWithIndex.map {
    case (arg: String, index) => ("p"+index, arg.trim.replaceAll("\\s{2,}", " "))
    case (arg, index) => ("p"+index, arg)
  }
  // Expands the Seq[Any] values with their names -> ("p0", v0), ("p1_0", v1_item0), ("p1_1", v1_item1), ...
  val onParams = params.flatMap {
    case (name, values: Seq[Any]) => values.zipWithIndex.map(v => (name+"_"+v._2, anorm.toParameterValue(v._1)))
    case (name, value) => List((name, anorm.toParameterValue(value)))
  }
  // Regenerates the original query substituting each argument by its name expanding Seq[Any] values separated by commas
  val query = (sc.parts zip params).map {
    case (s, (name, values: Seq[Any])) => s + values.indices.map(name+"_"+_).mkString("{", "},{", "}")
    case (s, (name, value)) => s + "{"+name+"}"
  }.mkString("") + sc.parts.last
  // Creates the anorm.Sql
  anorm.SQL(query).on(onParams:_*)
}
```

And you can use it:

```
val carIds = List(1, 3, 5)
SQLin"select * from car where id in ($carIds)".as(Car.simple *)
```

Adrian Hurtado
https://groups.google.com/forum/#!topic/play-framework/Q7XetWpD0A8
