

int check_overflow(int a, int b, int* res) 
{
  *res = a + b; 

  return (a < 0 && b < 0 && *res > 0) || (a > 0 && b > 0 && *res < 0) ;
}
