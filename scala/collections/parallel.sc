//
// Concurrency Level for parallel collection (par)
//
// See more ->
// https://stackoverflow.com/questions/9154691/how-to-set-the-number-of-threads-to-use-for-par?noredirect=1
def withParallelism[A](n : Int)(block : => A) : A = {
  import collection.parallel.ForkJoinTasks.defaultForkJoinPool._
  val defaultParLevel = getParallelism
  setParallelism(n)
  val ret = block
  setParallelism(defaultParLevel)
  ret
}

withParallelism(2) {
  (1 to 100).par.map(_ * 2)
}
