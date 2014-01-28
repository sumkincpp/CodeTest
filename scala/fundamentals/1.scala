/*
* matching desired type with match
*/
def makeOption(a: Any): Option[Any] = a match {
  case opt: Option[_] => opt
  case _ => Some(a) // Or Option(a), to eliminate the evil Some(null)
}
