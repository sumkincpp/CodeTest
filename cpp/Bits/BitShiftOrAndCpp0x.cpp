/*
 * g++ -std=c++0x BitShiftOrAndCpp0x.cpp -o BitShiftOrAndCpp0x
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

#include <chrono>

using std::cout;

namespace sc = std::chrono;

inline sc::milliseconds current_millis() {
  auto time = sc::system_clock::now(); // get the current time
  auto since_epoch = time.time_since_epoch(); // get the duration since epoch

  // I don't know what system_clock returns
  // I think it's uint64_t nanoseconds since epoch
  // Either way this duration_cast will do the right thing
  auto millis = sc::duration_cast<sc::milliseconds>(since_epoch);
  return millis.count();
}

inline sc::milliseconds get_exec_time (void (*func)()) {
    long now = current_millis(), final; // just like java (new Date()).getTime();
    func();
    final = current_millis() - now;
    return final;
}

inline int myrand() {
  // TBD
  return 42; // first time it is unpredicatable number
}

int main () {
    srand(time(0));

    const int N = 100000000;

    cout << get_exec_time ([] () {
        for (int i = 0; i < N; i++) {
            int a = myrand();
            (a & 1);
        }
    });

    cout << std::endl << "----------------" << std::endl;

    cout << get_exec_time ([] () {
        for (int i = 0; i < N; i++) {
            int a = myrand();
            (a >> 1) << 1;
        }
    });

    cout << std::endl << "----------------" << std::endl;

    cout << get_exec_time ([] () {
        for (int i = 0; i < N; i++) {
            int a = myrand();
            (a % 2);
        }
    });
}
