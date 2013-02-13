    #include <iostream>
#include <functional>

using std::cout;

void foo() { cout << "FOOEE!"; }

void  bar (void (*func)()) { func(); }
void bar2 (std::function<void(void)> f2) { f2(); }

int main () {

    // 1. Passing raw function pointer
    bar(foo);
    bar2(foo);

    // 2. Raw lambda call
    bar( [] () { cout << "FCUK YEAH!"; } );
    bar2( [] () { cout << "FCUK YEAH!"; } );

    // 3. lambda with auto -> function pointer
    auto f2 = [] () { cout << "f2!"; };
    bar(f2);
    bar2(f2);

    // 4. Passing std::function
    // !!! Will not compile
    // error: cannot convert 'std::function<void()>*' to
    //        'void (*)()' for argument '1' to 'void bar(void (*)())'|
    std::function<void(void)> f = [] () { cout << "fdjfklsdjl!"; };

    //bar(f); // FCUK - not compiling. Cannot convert std::function to function pointer

    bar2 (f); // OOK
}

