#include <iostream>

#define print(ar, n) { for (int k1 = 0; k1 < n; k1++) { cout << ar[k1] << " "; } cout << std::endl; }

using std::cout;

inline int  left(int i) { return 2*i + 1; }
inline int right(int i) { return 2*i + 2; }
inline int max_i(int* ar, int a, int b) { return ar[a] > ar[b] ? a : b; }

void heapify(int* ar, int i, int N) {
    int max_child = i;

    if (right(i) < N) max_child = max_i(ar, left(i), right(i));
    else if (left(i) < N) max_child = left(i);
    else return;

    if (ar[max_child] > ar[i]) {
        std::swap (ar[max_child], ar[i]);
        heapify (ar, max_child, N);
    }
}

void build_heap (int* ar, int N) {
    for (int i = N/2; i >= 0; i--) {
        heapify(ar, i, N);
    }
}

void heapsort (int* ar, int N) {
    build_heap(ar, N);
    print(ar, N);
    for (int i = N; i > 0; i--) {
        std::swap(ar[0], ar[i-1]);
        heapify(ar, 0, i-1);
    }
}

int main () {
    int ar[] = {0, 3, 5, -2, 3 , 6};
    int N = sizeof(ar)/sizeof(int);

    print(ar, N);
    heapsort(ar, N);
    print(ar, N);
}
