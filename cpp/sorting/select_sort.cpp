#include <iostream>

#include "utils.cpp"

// ~10 mins with error debugging
template <class T>
int minimum_i(T* ar, int l, int r) {
    int min_i = l;
    for (int i = l; i < r; i++) {
        if (ar[min_i] > ar[i]) min_i = i;
    }
    return min_i;
}

template <class T>
void selection_sort(T* ar, int sz) {
    for (int i = 0; i < sz; i++) {
        int min_i = minimum_i(ar, i, sz);
        std::swap(ar[i], ar[min_i]);
    }
}

int main () {
    int ar1[] = {-4, 6, -7, 3, 5, 2};
    int sz = sizeof(ar1)/sizeof(int);

    selection_sort(ar1, sz);
    print (ar1, sz);
}
