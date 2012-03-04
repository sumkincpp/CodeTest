#include <iostream>
#include <sstream>

using std::cout;
using std::string;
using std::stringstream;

 int main () {
    string hello = "1,2,3;hi there\nfsdfds\n";
    stringstream strm(hello);
    string other;

    int a = 0, b = 0, c = 0;
    char delim = '\0';

    strm >> a >> delim >> b >> delim >> c >> delim;
    getline (strm, other, '\n');
    // OR

    char* st = &other[0];
    cout << st;
    // sstrm.get (buf, '\n');
//    cout << other << "fsd";
}
