
################################################
#
# Check if array includes Range
#
################################################

['w', '-', 12].grep('a'..'z') # => ["w"]
[ 4 , :a, '^'].grep('a'..'z') # => []
['w', '-', 'e'].grep('a'..'z') # => ["w", "e"]

# Here is a modified code of your using #grep :

ary = ['w', '-', 12]
if ary.grep('a'..'z').empty?
  puts "Doesnt have Permutation"
else
  puts "Have permutation"
end  
