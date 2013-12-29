
// http://stackoverflow.com/questions/20262036/slick-query-multiple-tables-databases-with-getting-column-names/20278761#20278761
import scala.slick.jdbc.{GetResult,PositionedResult}
object ResultMap extends GetResult[Map[String,Any]] {
  def apply(pr: PositionedResult) = {
    val rs = pr.rs // <- jdbc result set
    val md = rs.getMetaData();
    val res = (1 to pr.numColumns).map{ i=> md.getColumnName(i) -> rs.getObject(i) }.toMap
    pr.nextRow // <- use Slick's advance method to avoid endless loop
    res
  }
}
val result = sql"select * from ...".as(ResultMap).firstOption

