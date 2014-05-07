

proc example {myArrName} {
     upvar 1 $myArrName myArr

     foreach elem [array names myArr] {
         puts $elem
     }
}

array set data {a 1 b 2 c 3}
example data

# -> a 1
#    b 2
#    c 3
