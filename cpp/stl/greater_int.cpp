#include <functional> 
#include <algorithm>
#include <vector>
  
int main()
{  
   vector<int> vi;
   vi.push_back(4);
   vi.push_back(1);
   vi.push_back(3);
   sort(vi.begin(), vi.end(), greater<int>() );
} 
