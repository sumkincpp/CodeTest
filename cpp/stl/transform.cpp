

std::transform(v1.begin(),v1.end(),std::back_inserter(v2), ExcitingUnaryFunctor());


// on set -- trick is to use std::inserter

std::set<int> s1, s2;
s1 = getAnExcitingSet();
std::transform(s1.begin(), s1.end(), std::inserter(s2, s2.begin()), ExcitingUnaryFunctor());
