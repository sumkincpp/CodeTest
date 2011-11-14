#include <iostream>

using std::cout;

template <int n>
class Fact {
public:
  static const int val = Fact<n-1>::val * n;
};

template<>
class Fact<0> { public: static const int val = 1; };

int main() {
  cout << Fact<7>::val;

  return 0;
}