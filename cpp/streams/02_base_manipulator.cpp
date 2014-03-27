#include <algorithm>
#include <cassert>
#include <climits>
#include <iomanip>
#include <iostream>
#include <locale>

struct base
{
   mutable std::ostream *_out;
   int _value;

   base(int value=10) : _value(value) {}

   template<typename T>
   const base& operator << (const T & data) const
   {
        *_out << data;
        return *this;
   }
   const base& operator << (const int & data) const
   {
        switch(_value)
        {
            case 2:
            case 4:
            case 8:  return print(data);
            case 16: *_out << std::hex << data; break;
            default:  *_out << data;
        }
        return *this;
   }
   const base & print(int data) const
   {
        int digits[CHAR_BIT * sizeof(int)], i = 0;
        while(data)
        {
             digits[i++] = data % _value;
             data /= _value;
        }
        while(i) *_out << digits[--i] ;
        return *this;
   }
   friend const base& operator <<(std::ostream& out, const base& b)
   {
       b._out = &out;
       return b;
   }
};

int main() {
   std::cout << base(2) << 255 <<", " << 54 << ", " << 20 << "\n";
   std::cout << base(4) << 255 <<", " << 54 << ", " << 20 << "\n";
   std::cout << base(8) << 255 <<", " << 54 << ", " << 20 << "\n";
   std::cout << base(16) << 255 <<", " << 54 << ", " << 20 << "\n";
}
