case class ExpirableMessage(enqueuedAt: Long, message: AnyRef)

class ExpirableActor extends Actor {

  case receive = {
    case ExpirableMessage(enqueuedAt, message) if enqueuedAt > Platform.currentTime - 5000 => { ... }
  }

}
