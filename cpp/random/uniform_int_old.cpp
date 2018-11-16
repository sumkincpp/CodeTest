// uniform_int_distribution
#include <iostream>
#include <random>

int main()
{
  const int nrolls = 10000; // number of experiments
  const int nstars = 95;    // maximum number of stars to distribute

  int p[10]={};

  for (int i=0; i<nrolls; ++i) {
    int number = rand() % 10;
    ++p[number];
  }

  std::cout << "uniform_int_distribution (0,9):" << std::endl;
  for (int i=0; i<10; ++i)
    std::cout << i << ": " << std::string(p[i]*nstars/nrolls,'*') << std::endl;

  return 0;
}
