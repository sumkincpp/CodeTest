#include <iostream>
#include <stdlib.h>
#include <time.h>

#define print_line() { cout << "---------------------------------" << std::endl; }

using std::cout;
using std::endl;

template <int> void print(int* ar, int n);
template <int> void fillrand(int* ar, int n);

template <class T>
void print(T* ar, int n) {
    for (int k1 = 0; k1 < n; k1++) {
        cout << ar[k1] << " ";
    }
    cout << std::endl;
}

template <class T>
void fillrand(T* ar, int n, int max = 100) {
    srand(time(0));
    for (int k = 0; k < n; k++) {
        ar[k] = rand() % max;
    }
}
