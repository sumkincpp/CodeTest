#include <iostream>

using std::cout;

struct A {
public :
    void move () { cout << "A::move()";}
    void move (int) { cout << "A::move(int)";}
};

struct B : A {
    void move () { cout << "B::move()";}
};


int main () {
    B b;
    b.move();
    b.A::move(2);
    b.move(2); //gcc -> error: no matching function for call to 'B::move(int)'

}
