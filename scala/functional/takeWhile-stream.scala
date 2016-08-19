val reader = new BufferedReader(new InputStreamReader(???))
val responseBuffer = new StringBuffer()

Iterator.continually(reader.readLine())
  .takeWhile(line => line != null && line.nonEmpty)
  .foreach { inputLine =>
    responseBuffer.append(inputLine)
  }

println(responseBuffer.toString())
/// or even
val inputStream = ???
val content = io.Source.fromInputStream(inputStream).getLines.mkString
inputStream.close
