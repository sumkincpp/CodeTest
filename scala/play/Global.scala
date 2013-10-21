
// Tracing `not found` files 
override def onHandlerNotFound(r: RequestHeader) = {
    if(Logger.isInfoEnabled) Logger.info("Not found: " + r.path)
    Future.successful(
      NotFound(views.html.error.missing(r.path))
    )
  }
