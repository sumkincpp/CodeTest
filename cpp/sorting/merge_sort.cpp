#include <iostream>

#include "utils.cpp"

const int N = 1000;

template <class T>
void merge(T* ar, int l, int r, int m) {
    if ((r - l) > N || l >= r) return;
    T aux[N] = {0};

    // first part
    for (int i = l; i < m; i++)
        aux[i] = ar[i];

    //second part - must be reversed
    for (int i = 0; i < r-m; i++)
        aux[m+i] = ar[r-1-i];

    int lc = l; // lc=left current
    int rc = r-1; // rc=right current

    for (int i = l; i < r; i++) {
        if (aux[lc] < aux[rc]) { ar[i] = aux[lc]; lc++; }
        else { ar[i] = aux[rc]; rc--; }
    }
}

template <class T>
void merge_sort(T* ar, int l, int r) {
    if (l >= r-1) return;
    int m = (l + r)/2;

    merge_sort(ar, l, m);
    merge_sort(ar, m, r);

    merge(ar, l, r, m);
}

int main () {
    int ar1[] = {-4, 6, -7, 3, 5, 2};
    int sz = sizeof(ar1)/sizeof(int);

    merge_sort(ar1, 0, sz);
    print (ar1, sz);
}

