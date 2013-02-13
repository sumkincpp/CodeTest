#include <iostream>
#include <limits>

template<typename>
struct to_string {
    // optionally, add other information, like the size
    // of the string.
    static char const* val() { return "unknown"; }
};

#define DEF_TYPE(X) \
    template<> struct to_string<X> { \
        static char const* val() { return #X; } \
    }

DEF_TYPE(int);
DEF_TYPE(float);
DEF_TYPE(double);
DEF_TYPE(long double);


using std::endl;
using std::cout;

template <class T>
void printCharacteristics() {
    cout << "=====================================" << endl;
    cout << "Type: "<< to_string<T>::val() << endl;
    cout << "sizeof(T): "<< sizeof(T) << endl;
    cout << "digits10: "<< std::numeric_limits<T>::digits10 << endl;
    cout << "radix: "<< std::numeric_limits<T>::radix << endl;
    cout << "min_exponent10: "<< std::numeric_limits<T>::min_exponent10 << endl;
    cout << "max_exponent10: "<< std::numeric_limits<T>::max_exponent10 << endl;
    cout << "epsilon: "<< std::numeric_limits<T>::epsilon() << endl;
    cout << "min: "<< std::numeric_limits<T>::min() << endl;
}

int main () {
    printCharacteristics<float>();
    printCharacteristics<double>();
    printCharacteristics<long double>();
}
