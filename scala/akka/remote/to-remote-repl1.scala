class TestActor extends Actor {
     def receive = {
       case x => println("Received: " + x.toString)
     }
   }

val system = ActorSystem("LocalSystem")
val remoteActor = system.actorFor("akka.tcp://application@<host>:110/user/main")

implicit val sender = system.actorOf(Props(classOf[TestActor]), "testActor")

remoteActor ! "Everybody been there!"
