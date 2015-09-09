//-----------------------------------------------------
#include <algorithm>

std::string s = "a_b_c";
size_t n = std::count(s.begin(), s.end(), '_');
//-----------------------------------------------------

std::string::iterator end_pos = std::remove(str.begin(), str.end(), ' ');
str.erase(end_pos, str.end());

string.erase(std::remove_if(string.begin(), string.end(), std::isspace), string.end()); // ? is _if legal

//-----------------------------------------------------
// Splitting string to vector with char delimiter
#include <string>
#include <sstream>
#include <vector>

std::vector<std::string> &split(const std::string &s, char delim, std::vector<std::string> &elems) {
    std::stringstream ss(s);
    std::string item;
    while (std::getline(ss, item, delim)) {
        elems.push_back(item);
    }
    return elems;
}

std::vector<std::string> split(const std::string &s, char delim) {
    std::vector<std::string> elems;
    split(s, delim, elems);
    return elems;
}

// Also, thi will keep empty tokens
// https://stackoverflow.com/questions/236129/split-a-string-in-c
std::vector<std::string> x = split("one:two::three", ':');
