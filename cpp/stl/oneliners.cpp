/**
  * C++ STL oneliners
  */
  
// Appending a vector to a vector
a.insert(a.end(), b.begin(), b.end());

std::copy (b.begin(), b.end(), std::back_inserter(a));

std::string the_prefix_you_want = string1.substr(0, string1.find("%"));
