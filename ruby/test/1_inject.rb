def split_and_sum(string)
  string.split(",").collect { |i| i.to_i }.inject(:+)
end
