#include <thrust/host_vector.h>
#include <thrust/iterator/zip_iterator.h>
#include <thrust/iterator/counting_iterator.h>
#include <thrust/sequence.h>
#include <thrust/copy.h>

#define N 30
#define SELECT 3

typedef thrust::tuple<int, int>            tpl2int;
typedef thrust::host_vector<int>::iterator intiter;
typedef thrust::counting_iterator<int>     countiter;
typedef thrust::tuple<intiter, countiter>  tpl2intiter;
typedef thrust::zip_iterator<tpl2intiter>  idxzip;


struct select_unary_op : public thrust::unary_function<tpl2int, int>
{
  __host__ __device__
  int operator()(const tpl2int& x) const
  {
    if ((x.get<1>() %SELECT) == 0)
      return x.get<0>();
    else return -1;
   }
};

int main() {

  thrust::host_vector<int> A(N);
  thrust::host_vector<int> result(N);
  thrust::sequence(A.begin(), A.end());
  thrust::counting_iterator<int> idxfirst(0);
  thrust::counting_iterator<int> idxlast = idxfirst +N;

  idxzip first = thrust::make_zip_iterator(thrust::make_tuple(A.begin(), idxfirst));
  idxzip  last = thrust::make_zip_iterator(thrust::make_tuple(A.end(), idxlast));
  select_unary_op my_unary_op;

  thrust::transform(first, last, result.begin(), my_unary_op);
  std::cout << "Results :" << std::endl;
  thrust::copy(result.begin(), result.end(), std::ostream_iterator<int>( std::cout, " "));
  std::cout << std::endl;


  return 0;

}