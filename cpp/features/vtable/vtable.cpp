//#define DUMP_MODE

#ifdef DUMP_MODE

#include <iostream>
using std::cout;

#endif

struct A1 {
    void foo();
};

struct B1 : A1 {
    void foo();
};

struct A2 {
    virtual void foo() {}
};

struct B2 : A2 {
    void foo() {}
};


int main () {
#ifdef DUMP_MODE
    {
        A1 a;
        std::cout << sizeof(a) << " --- " << sizeof(A1) << std::endl;
    }
    {
        B1 a;
        std::cout << sizeof(a) << " --- " << sizeof(B1) << std::endl;
    }
    {
        A2 a; // virtual - позднее связывание, late binding
        std::cout << sizeof(a) << " --- " << sizeof(A2) << std::endl;
    }
    {
        B2 b; // virtual - позднее связывание, late binding
        std::cout << sizeof(b) << " --- " << sizeof(B2) << std::endl;
    }
#endif
}
