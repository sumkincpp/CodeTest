import akka.actor.{ ActorSystem, Props }
import spray.can.Http
import com.typesafe.config.ConfigFactory
import java.security.Security
import akka.actor.ActorRef
import akka.routing.RoundRobinRouter
import akka.io.IO

object Boot extends App {
  new ProxyKernel().startup()
}
