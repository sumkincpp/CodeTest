// executeQuery comprehensions
// see more : http://stackoverflow.com/questions/17276649/scala-elegant-list-comprehension-as-in-f
val rs = stmt.executeQuery
val it = Iterator.continually(if (rs.next()) Some(rs.getInt(1)) else None)
val result = it.takeWhile(_.isDefined).toList.flatten
