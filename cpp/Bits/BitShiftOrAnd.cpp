/*
 *
&     1.895
----------------
>> << 1.898
----------------
% 2   1.854
*/

#include <iostream>
#include <time.h>
#include <stdlib.h>

using std::cout;

long double get_exec_time (void (*func)()) {
    clock_t init = clock(), final;
    func();
    final = clock() - init;
    return (double)final / ((double)CLOCKS_PER_SEC);
}

int main () {
    srand(time(0));

    const int N = 100000000;

    cout << get_exec_time ([] () {
        for (int i = 0; i < N; i++) {
            int a = rand();
            (a & 1);
        }
    });

    cout << std::endl << "----------------" << std::endl;

    cout << get_exec_time ([] () {
        for (int i = 0; i < N; i++) {
            int a = rand();
            (a >> 1) << 1;
        }
    });

    cout << std::endl << "----------------" << std::endl;

    cout << get_exec_time ([] () {
        for (int i = 0; i < N; i++) {
            int a = rand();
            (a % 2);
        }
    });
}
