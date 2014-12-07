#include <iostream>

int main()
{
  int arr[] = {0, 1, 2, 3, 4, 5};
  
  
  int total = std::accumulate(arr, arr+6, 0);
  std::cout << total << endl; 
  
  int sum  = 0;
  std::for_each(arr, arr+6, [&sum](int n){ sum += n; });
  std::cout << sum;
  
  sum  = 0;
  std::cout << std::for_each(arr,arr+6,[&](int n)->int{sum += n;return sum;})(0);
  
  return 0;
}
