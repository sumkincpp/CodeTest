// http://www.cebix.net/pipermail/ginac-list/2013-February/001949.html
//
#include <iostream>
#include <ginac/ginac.h>
using namespace std;
using namespace GiNaC;

DECLARE_FUNCTION_1P( GA );
REGISTER_FUNCTION( GA, dummy() );

DECLARE_FUNCTION_3P( JF1 );
REGISTER_FUNCTION( JF1, dummy() );

int main()
{
     symbol a("a");
     symbol b("b");
     symbol t("t");
     symbol x("x");
     symbol y("y");
     ex temp = JF1(a, GA(t), b)*JF1(x, GA(t), y);
     cout << temp << endl;
     cout << temp.has( JF1(wild(1), GA(wild(5)), wild(2)) *
                       JF1(wild(3), GA(wild(5)), wild(4)),
                       has_options::algebraic ) << endl;
     cout << temp.subs(JF1(wild(1), GA(wild(5)), wild(2)) *
                       JF1(wild(3), GA(wild(5)), wild(4)) == 2,
                       subs_options::algebraic ) << endl;
}
