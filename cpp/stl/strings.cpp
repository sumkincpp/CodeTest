//-----------------------------------------------------
#include <algorithm>

std::string s = "a_b_c";
size_t n = std::count(s.begin(), s.end(), '_');
//-----------------------------------------------------

std::string::iterator end_pos = std::remove(str.begin(), str.end(), ' ');
str.erase(end_pos, str.end());

string.erase(std::remove_if(string.begin(), string.end(), std::isspace), string.end()); // ? is _if legal

//-----------------------------------------------------
