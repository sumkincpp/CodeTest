#include <iostream>
#include <functional>

struct A {
  int a;
  
  A():a(100) {}
  
  int func(int b, char c) {
    std::cout << a << " - " << b << " - " << c << " -- ey!" << std::endl;
  }
  
};

int main() {
  A a;
  std::function<int(int, char)> func;

  func = std::bind(&A::func, &a, std::placeholders::_1, std::placeholders::_2);

  func(10, '2');
}
