#include <iostream>

using std::cout;

int fastpow1 (int n, int power)
{ 
  if (power == 1) return n;
  return (power % 2 == 0 ? fastpow1(n*n, power/2) : n*fastpow1(n, power-1));
}

//tail-recursion
int fastpow2 (int n, int power, int acc) 
{
  if (power == 1) return n*acc;

  if (power % 2 == 0)
    return fastpow2 ( n*n, power/2, acc);
  else
    return fastpow2 ( n, power-1, acc*n);
}

int fastpow2 (int n, int power) 
{
  return fastpow2(n, power, 1);
}

int main () 
{
  int (*powf)(int, int) = fastpow2;

	cout << powf(2, 1);
	cout << powf(2, 2);
	cout << powf(2, 3);
	cout << powf(2, 4);
}
