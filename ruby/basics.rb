
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

"hello James!".downcase 
"hello James!".upcase
"hello James!".capitalize

### Dates ###

Date.today.month         # => current month(int)
Date::MONTHNAMES[1]      # => January
Date::ABBR_MONTHNAMES[1] # => JAN

### Arrays / Enumerators ###

(1..6).group_by { |i| i%3 } # => {0=>[3, 6], 1=>[1, 4], 2=>[2, 5]}
(1..10).each_slice(3).to_a  # => [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]


### Files ###

# File size in MBs
compressed_file_size = '%.2f' % (File.size("file.txt").to_f / 2**20)
# in bytes
File.stat("testfile").size

# Touch File
require 'fileutils'
FileUtils.touch('file.txt')  #1

File.open("foo.txt", "w") {} #2
File.write("foo.txt", "")    #3

# Glob files

Dir["config.?"]                     #=> ["config.h"]
Dir.glob("config.?")                #=> ["config.h"]


12.method("+").call(3) # => 15
