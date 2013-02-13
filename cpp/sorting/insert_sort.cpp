#include <iostream>

#include "utils.cpp"

//Wrote it in 3 mins :D
template <class T>
void insert_sort (T* ar, int sz) {
    for (int i = 1; i < sz; i++) {
        for (int k = i; k > 0; k--) {
            if (ar[k] < ar[k-1]) std::swap(ar[k], ar[k-1]);
        }
    }
}


int main () {
    int ar1[] = {-4, 6, -7, 3, 5, 2};
    int sz = sizeof(ar1)/sizeof(int);

    insert_sort(ar1, sz);
    print (ar1, sz);
}
