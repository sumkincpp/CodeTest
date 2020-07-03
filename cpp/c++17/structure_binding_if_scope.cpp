#include <iostream>
#include <map>
#include <set>

int main() {
  std::cout << "Hello World!\n";

  std::map<std::string, size_t> animal_population {
    {"humans", 7000000000},
    {"chickens", 17863376000},
  };

  //==========================================================================
  // C++17 Using structured bindings to unpack bundled return values
  //==========================================================================
  for (const auto &[species, count] : animal_population) {
    std::cout << "There are " << count << " " << species
              << " on this planet.\n";
  }
  {
    std::tuple<int, float, long> tup {1, 2.0, 3};

    auto [a, b, c] = tup;
  }

  // Before C++17
  std::tuple<int, int> result {11, 5};

  int remainder;
  std::tie(std::ignore, remainder) = result;
  std::cout << "remainder is " << remainder << '\n';

  //==========================================================================
  // Limiting variable scopes to if and switch statements
  //==========================================================================
  std::map<char, int> character_map = {{'c', 2}, {'a', 3}};

  if (auto itr (character_map.find('c')); itr != character_map.end()) {
    // *itr is valid. Do something with it.
    std::cout << itr->second << '\n';
  } else {
    // itr is the end-iterator. Don't dereference.
    std::cout << "It's an end!" << '\n';
  }

  // wont work
  //const auto &[a, b] = character_map.find('c');
  
  switch (const auto c {'a'}; c) {
    case 'a': break;
    case 'b': break;
    default:
      std::cout << "invalid input: " << c << '\n';
  }

  std::cout << "Finish!" << '\n';
  // itr is not available here at all
}
