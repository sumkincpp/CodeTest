package controllers
 
import play.api.mvc.{Controller, Action, Result}
import play.api.libs.ws.WS
import play.api.libs.json.Json
import play.api.libs.concurrent.Execution.Implicits._
import scala.concurrent.Future
 
object Race extends Controller {
  def index() = Action {
    Async {
      val start = System.currentTimeMillis()
      def getLatency(r: Any): Long = System.currentTimeMillis() - start
      val googleTime = WS.url("http://www.google.com").get().map(getLatency)
      val yahooTime = WS.url("http://www.yahoo.com").get().map(getLatency)
      val bingTime = WS.url("http://www.bing.com").get().map(getLatency)
       
      Future.sequence(Seq(googleTime, yahooTime, bingTime)).map { case times =>
       Ok(Json.toJson(Map("google" -> times(0), "yahoo" -> times(1), "bing" -> times(2))))
      }
    }
  }
}
