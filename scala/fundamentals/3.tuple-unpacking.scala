def foo(a:Int, b:Int) = {}

foo(a,b) //right way to invoke foo

# getParams tuple
def getParams = {
   //Some calculations
   (a,b)  //where a & b are Int
}

(foo _).tupled(getParams)
