import akka.kernel.Bootable
import akka.actor.{ ActorSystem, Props }
import akka.actor.ActorRef
import akka.io.IO
import akka.routing.RoundRobinRouter
import org.slf4j.LoggerFactory
import spray.can.Http

case object Start

class ProxyKernel extends Bootable {

  private val logger = LoggerFactory.getLogger(this.getClass())

  implicit val system = ActorSystem()

  def startup = {
    val host = sys.props.getOrElse("service.host", "localhost")
    val port = sys.props.getOrElse("service.port", "8080").toInt

    logger.warn(f"service bind to ${host}:${port}")

    val numActors = sys.props.getOrElse("service.num_actors", "5").toInt

    var routees = List[ActorRef]()
    for (i <- 1 until numActors) {
      val actor = system.actorOf(Props[RedirectorServiceActor])
      routees = actor :: routees
    }

    val service = system.actorOf(Props[RedirectorServiceActor].withRouter(RoundRobinRouter(routees)))

    IO(Http) ! Http.Bind(service, interface = host, port = port)
  }

  def shutdown = {
    system.shutdown()
  }

}
