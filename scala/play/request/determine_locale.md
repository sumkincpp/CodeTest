# Determine locale in Play! Framework

// original by Fernando Correia <fernandoacorreia@gmail.com> 

This implicit function will create the best-fitting Lang object for a request, according to the rules of the Play framework:

https://github.com/playframework/playframework/blob/master/framework/src/play/src/main/scala/play/api/mvc/Controller.scala?source=cc#L64

When you have this Lang object, you can get the language with "lang.code".

For an example see this code:

    package controllers
    
    import play.api._
    import play.api.mvc._
    import play.api.i18n.Lang
    
    object Application extends Controller {
    
      def index = Action { implicit request =>
        val conf = getConfig("application.langs").get
        val acc = acceptedLanguages(request)
        val pref = preferredLanguage
        Ok(s"application.langs = '$conf'; accepted languages = '$acc'; selected language = '$pref'")
      }
    
      private def getConfig(key: String) = Play.maybeApplication.flatMap(_.configuration.getString(key))
    
      private def acceptedLanguages(request: RequestHeader) = request.acceptLanguages.map(_.code).mkString(", ")
    
      private def preferredLanguage()(implicit lang: Lang) = lang.code
    }

To test it, in application.conf set:

application.langs="en,pt-BR"

Then start the Play application and in a separate command prompt run:

    $ curl -H "Accept-Language: pt-BR,en;q=0.5" http://localhost:9000
    
    application.langs = 'en,pt-BR'; accepted languages = 'pt-BR, en'; selected language = 'pt-BR'

    $ curl -H "Accept-Language: en,pt-BR;q=0.5" http://localhost:9000
    
    application.langs = 'en,pt-BR'; accepted languages = 'en, pt-BR'; selected language = 'en'

Please notice that the conversion function will only run in a Controller class with an implicit request object in context, such as in the example above.
