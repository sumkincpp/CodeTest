/**
  * http://www.playframework.com/documentation/2.2.x/ScalaHttpFilters
  */

object LoggingFilter extends Filter {
  
  override def apply(next: (RequestHeader) => Future[SimpleResult])(rh: RequestHeader) = {
    val start = System.currentTimeMillis

    def logTime(result: SimpleResult): Result = {
      val time = System.currentTimeMillis - start
      Logger.info(s"${rh.method} ${rh.uri} took ${time}ms and returned ${result.header.status}")
      result.withHeaders("Request-Time" -> time.toString)
    }

    val resultF = next(rh) 
    resultF foreach logTime 
    resultF
  }
}
