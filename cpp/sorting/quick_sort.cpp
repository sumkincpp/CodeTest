#include <iostream>

#include "utils.cpp"

template <class T>
int partition(T* ar, int l, int r) {
    if (l >= r-1) return l;

    int l1 = l;
    for (int r1 = r-2; l1 <= r1; l1++, r1--) {
        // Going from left to right - first index
        while(l1 <= r1 && ar[l1] < ar[r-1]) l1++;
        // oops, stuck on a limit
        if (l1 > r1) break;

        // Going from right to left - second index
        while(r1 > l1 && ar[r1] > ar[r-1]) r1--;
        if (r1 == l1) break;

//        cout << l1 << " " << r1 << endl;
//        cout << "ar" << ar[l1] << " " << ar[r1] << endl;
        cout << "(" << ar[l1] << "," << ar[r1] << ")" << endl;
        print (ar+l, r-l);
        std::swap(ar[l1], ar[r1]);
    }
    cout << l1 << "s" << endl;
    if (ar[l1] > ar[r-1])
        std::swap(ar[l1], ar[r-1]);

    return l1;
}
//
template <class T>
void quick_sort(T* ar, int l, int r) {
    if (l >= r-1) return;

    print (ar+l, r-l);
    int m = partition(ar, l, r);
    print (ar+l, r-l);
    print_line();
    quick_sort(ar, l, m);
    quick_sort(ar, m+1, r);
}



int main () {
    const int sz = 100;
//    int ar1[sz] = {86, 89, 1, 50, 57, 52, 89, 95, 86, 58};
//    int ar1[sz] = {59, 94, 86, 24, 74, 21, 50, 98, 69, 26};
    int ar1[sz];
    fillrand(ar1, sz);


    print (ar1, sz);
    quick_sort(ar1, 0, sz);
    print (ar1, sz);
}
