#include <iostream>

using std::cout;

int main () {
        int size = 10;
        int* a = new int[size*size];
        delete[] a;
        ///OR
        int** b = new int*[size];

        for (int i = 0; i < size; i++)
            b[i] = new int[size];


        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                b[i][j] = (i+j)%10;
                cout << b[i][j] << " ";
                }
            cout << std::endl;
            }

        for (int i = 0; i < size; i++)
            delete[] b[i];

        delete[] b;

}
