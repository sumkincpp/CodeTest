val configThing = Play.application.configuration.getString("configThing.key").getOrElse(throw new RuntimeException("Setting configTHing.key not defined"))

...

def stringSetting(key: String): String = Play.application.configuration.getString(key).getOrElse(throw new RuntimeException(s"Setting $key not defined"))
val configThing = stringSetting("configThing.key")


Play.current.configuration.getString("db.driver")
