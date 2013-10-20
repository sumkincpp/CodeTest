#include <thrust/host_vector.h>
#include <thrust/device_vector.h>
#include <thrust/iterator/zip_iterator.h>
#include <thrust/iterator/counting_iterator.h>
#include <thrust/sequence.h>
#include <thrust/copy.h>
#include <math.h>


#define K 8
#define N pow(2, K)

typedef thrust::tuple<int, float>            tpl2int;
typedef thrust::device_vector<float>::iterator intiter;
typedef thrust::counting_iterator<int>     countiter;
typedef thrust::tuple<intiter, countiter>  tpl2intiter;
typedef thrust::zip_iterator<tpl2intiter>  idxzip;

__host__ __device__
int isbitset (int val, int bitnum)
{
  return (val & (1 << bitnum)) != 0;
}
__host__ __device__
int get_spin(int val, int spin_number) 
{
  if (isbitset(val, spin_number)) return 1;
  else return -1;
}

struct Ising2DStep : public thrust::unary_function<tpl2int, int>
{
  
  float _j1;
  float _j2;

  Ising2DStep(float j1, float j2) : _j1(j1), _j2(j2) {}

  __host__ __device__
  float operator()(const tpl2int& x) const
  {
    int idx = x.get<1>();
    float val = x.get<0>();

    return val + _j1*get_spin(idx, 0)*get_spin(idx, 1) + _j2*get_spin(idx, 0)*get_spin(idx, K);
  }
};

inline int gen_j () { return (rand() % 2) * 2 - 1; }

int main() 
{

  thrust::device_vector<float> source(N);
  //thrust::sequence(source.begin(), source.end());
  thrust::fill(source.begin(), source.end(), 0);

  thrust::device_vector<float> result(N);
  thrust::counting_iterator<int> idxfirst(0);
  thrust::counting_iterator<int> idxlast = idxfirst + N;

  for (int i = 0; i < 10000; ++i) {
    // We copy same numbers to the end of vector to reduce them later => 2*2^K
    source.insert(source.end(), source.begin(), source.end());

    idxzip first = thrust::make_zip_iterator(thrust::make_tuple(source.begin(), idxfirst));
    idxzip  last = thrust::make_zip_iterator(thrust::make_tuple(source.end(), idxlast));

    int j2 = gen_j();

    //if (i % K == 0) j2 = 0;

    Ising2DStep isingStep(gen_j(), j2);

    // Here we are getting 2*2^K numbers that should reduced to 2^K
    thrust::transform(first, last, result.begin(), isingStep);

    source.clear();

    // Following the pattern -> we find minimum of pairs
    for (thrust::device_vector<float>::iterator it = result.begin(); it != result.end(); it += 2) {
      source.push_back (min( *it, *(it+1)));
    }

    /*for (thrust::device_vector<float>::iterator it = source.begin(); it != source.end(); it += 1) {
      std::cout << *it << " ";
    }
    std::cout << std::endl;*/

    //if ( i == 10) break;
  }
  // Printing values from source
  thrust::copy(source.begin(), source.end(), std::ostream_iterator<float>( std::cout, " "));


  return 0;

}