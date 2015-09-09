#include <boost/algorithm/string.hpp>

std::vector<std::string> strs;
boost::split(strs, "string to split", boost::is_any_of("\t "));
