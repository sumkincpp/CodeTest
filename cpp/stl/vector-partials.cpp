
// copy contents from one vector to another
a.insert(a.end(), b.begin(), b.end());

std::copy (b.begin(), b.end(), std::back_inserter(a));

// printing vec
std::copy(folders_vec.begin(), folders_vec.end(), std::ostream_iterator<std::string>(std::cout,", "));
