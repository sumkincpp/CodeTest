//--------------------------------------------------------------------------------------

scala> Map[String,Any]()
res24: scala.collection.immutable.Map[String,Any] = Map()

scala> type PropertyMap = Map[String, Any]
defined type alias PropertyMap

scala> PropertyMap()
<console>:12: error: not found: value PropertyMap
       PropertyMap()
       ^

scala> object PropertyMap {
     | def apply() = Map[String,Any]()
     | }
defined object PropertyMap

scala> PropertyMap()
res26: scala.collection.immutable.Map[String,Any] = Map()

//--------------------------------------------------------------------------------------
scala> type Meow = Map[Int, String]
defined type alias Meow

scala> new Meow()
<console>:13: error: trait Map is abstract; cannot be instantiated
       new Meow()
       ^
//--------------------------------------------------------------------------------------
