import akka.actor.Actor.Receive
import akka.actor.ActorContext
import akka.actor.ActorLogging
import akka.actor.Actor
import akka.event.LoggingAdapter

object MyLoggingReceive {

  def apply(log: LoggingAdapter)(r: Receive)(implicit context: ActorContext): Receive = r match {
    case _: MyLoggingReceive ⇒ r
    case _ ⇒
      if (context.system.settings.config.getBoolean("myloggingreceive")) new MyLoggingReceive(log, r) else r
  }
}

class MyLoggingReceive(log: LoggingAdapter, r: Receive) extends Receive {
  def isDefinedAt(o: Any): Boolean = {
    val handled = r.isDefinedAt(o)
    log.info("received {} message {}", if (handled) "handled" else "unhandled", o)
    handled
  }
  def apply(o: Any): Unit = r(o)
}

class MyActor extends Actor with ActorLogging {
  def receive = MyLoggingReceive(log) {
    case msg ⇒
  }
}
