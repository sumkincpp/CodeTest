list.foldLeft(0)((b,a) => b+a)
list.foldLeft(1)((b,a) => b*a)
list.foldLeft(List[Int]())((b,a) => a :: b)
