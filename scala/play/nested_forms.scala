  val cdForm = Form(
    mapping(
      "id" -> ignored(-1L),
      "title" -> text,
      "artist" -> text,
      "tracks" -> list(mapping(
        "title" -> text,
        "artist" -> optional(text),
        "length" -> optional(number)
      )(Track.apply)(Track.unapply))
    )(CompactDisc.apply)(CompactDisc.unapply)
  )
