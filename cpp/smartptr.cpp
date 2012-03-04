#include <iostream>
#include <math.h>

using namespace std;

struct Point {
    Point(int x = 0, int y = 0) : _x(x), _y(y) {}
    double operator () () { return sqrt (_x*_x + _y*_y); }
    double eval () { return sqrt (_x*_x + _y*_y); }


    int _x, _y;
};

template <class T>
struct SmartPointer {
    T* _data;
    SmartPointer(T* data): _data(data) {}
    ~SmartPointer() { cout << "destructor" << endl; delete _data; }

    T& operator* () { cout << "operator*"; return *_data; }
    T* operator-> () { cout << "operator->"; return _data; }
};

typedef char *(*(**SuperType[8][8])())[];

void foo2(SuperType s) {
    cout << "foo2";
}


int main () {
/*    SmartPointer<Point> ptr(new Point(3, 4));

    cout << (*ptr).eval() << endl;
    cout << ptr->eval();

//    char *(*(**foo[8][8])())[2];
*/
    typedef double (*func)(double);

    func f[2] = { sin, cos };

    struct MenuItem {
        char name[100];
        func f;
    };

    MenuItem ar[2] = {
        {"Start", sin},
        {"Exit", cos}
        };

    cout << f[1](3.14159265);

//    *foo[0] =

//    foo2(foo);
}

