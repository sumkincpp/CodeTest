
#include <boost/regex.hpp>

std::string result = boost::regex_replace(str, boost::regex("from"), "to");

#include<boost/algorithm/string/replace.hpp>
#include <boost/algorithm/string/erase.hpp>

boost::algorithm::erase_all_copy( s4, " " );
boost::algorithm::replace_all_copy( s4, "    ", "");

std::sort(a.begin(), a.end(), 
          boost::bind(&std::pair<int, int>::second, _1) <
          boost::bind(&std::pair<int, int>::second, _2));
          
//-------------------------------------
#include <boost/lexical_cast.hpp>
#include <string>

int main()
{
   float f = 1.2;
   int i = 42;
   std::string sf = boost::lexical_cast<std::string>(f); //sf is "1.2"
   std::string si = boost::lexical_cast<std::string>(i); //sf is "42"
}

//-------------------------------------

#include <boost/filesystem.hpp>

namespace fs = boost::filesystem;

int main ()
{
    fs::path dir ("/tmp");
    fs::path file ("foo.txt");
    fs::path full_path = dir / file;
    std::cout << full_path << std::endl;
}
//-------------------------------------
boost::filesystem::path config_folder(path_str);

if( !(boost::filesystem::exists(config_folder))) {
}

boost::filesystem::create_directories("/tmp/a/b/c");
