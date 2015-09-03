// https://stackoverflow.com/questions/2602013/read-whole-ascii-file-into-c-stdstring

#include <string>
#include <fstream>
#include <streambuf>

std::ifstream t("file.txt");
std::string str((std::istreambuf_iterator<char>(t)),
                 std::istreambuf_iterator<char>());

// -------------------------------------------------------------
// pre-allocation

#include <string>
#include <fstream>
#include <streambuf>

std::ifstream t("file.txt");
std::string str;

t.seekg(0, std::ios::end);   
str.reserve(t.tellg());
t.seekg(0, std::ios::beg);

str.assign((std::istreambuf_iterator<char>(t)),
            std::istreambuf_iterator<char>());
