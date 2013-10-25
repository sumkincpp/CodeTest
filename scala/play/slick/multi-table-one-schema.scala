class Users(schema:Option[String] = None) extends Table[(String, Int)](schema, "users") {
  def id = column[Int]("id")
  def name = column[String]("name")
  def * = name ~ id
}
object Schema {
  val users1 = new Users(Some("schema1"))
  val users2 = new Users(Some("schema2"))
}
