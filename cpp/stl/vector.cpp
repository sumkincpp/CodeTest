#include <vector>
#include <iostream>
#include <algorithm>
#include <functional>
#include <time.h>
#include <stdlib.h>

using namespace std;

void print_a (int a) {
    cout << "print_a : " << a << endl;
}

struct func_obj_print {
    int _sum;
    func_obj_print(int sum = 0) : _sum(sum) { }

    void operator () (int a) {
        _sum += a;
        cout << a << endl;
        cout << "sum = " << _sum << endl;
    }
};

/**
 * @author Fedor
 * @param argc number of elements ..
 * @param argc number of elements ..
 */
int main (int argc, char** argv) {
/*    func_obj_print f;
    f(100);
    f(10);
    f(130);
    cout << f._sum; */

/*    srand(time(0));

    vector<int> v;

    for (int i = 0; i < 100; i++) {
        v.push_back(rand()%10);
    }
*/
/*    for (int i = 0; i < v.size(); ++i ){
        cout << v[i] << endl;
    }
*/
//    for_each(v.begin(), v.end(), [](int a) { cout << "lambda :" << a << endl; } );
//    for_each(v.begin(), v.end(), print_a );
//    for_each(v.begin(), v.end(), func_obj_print() );
//
//
//    int array [] = { 1, 4, 9, 16 };
//
//    vector<int> v2 (array, array + 4);
//
//    v2.erase ();
///*    v2.erase (v2.begin ());
//    v2.erase (v2.end () - 1);
//    v2.erase (v2.begin () + 1, v2.end () - 1);
//*/
///*    v.insert (v.begin (), 0);
//    v.insert (v.begin (), v2.begin(), v2.end());
//*/
//    v.assign(v2.begin(), v2.end());
//
//    for_each(v.begin(), v.end(), print_a );
    vector<int> v;
    cout << "capacity = " << v.capacity () << endl;
    v.push_back (42);
    v.push_back (42);
    v.push_back (42);
    cout << "capacity = " << v.capacity () << endl;
    v.reserve (5000);
    cout << "capacity = " << v.capacity () << endl;
}
