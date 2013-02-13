#include <iostream>
#include <functional>

using std::cout;

void foo() {
    cout << "FOOEE!";
}

void bar (void (*func)()) {
    func();
}
void bar2 (std::function<void(void)> f2) {
    f2();
}

int main () {
    bar(foo);
    bar( [] () -> void { cout << "FCUK YEAH!"; });

    bar( [] () { cout << "FCUK YEAH!"; });

    std::function<void(void)> f1 = [] () { cout << "fdjfklsdjl!"; };
    auto f2 = [] () { cout << "fdjfklsdjl!"; };

//    bar (f1); // FCUK - not compiling. Cannot convert std::function to function pointer

    bar2 (f1); // OOK
    bar (f2);// OOK
}
