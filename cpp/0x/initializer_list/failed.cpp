#include <initializer_list>
#include <string>
#include <iostream>

template <typename T>
struct container
{
    void insert(T const& x)
    {
        std::cout << "1" << std::endl;
    }

    void insert(std::initializer_list<T> x) {
        std::cout << "2" << std::endl;
    }

    template <typename T1>
    void insert(std::initializer_list<T1> x) {
        std::cout << "3" << std::endl;
    }
};

int main()
{
    container<std::string> c;

    std::cout << "String literal:\n";
    c.insert("a");

    std::cout << "std::string:\n";
    c.insert(std::string("a"));

    std::cout << "initializer list of std::string:\n";
    c.insert({std::string("a"), std::string("b")});

    std::cout << "initializer list of string literals:\n";
    c.insert({"a"});
    c.insert({"a", "b"});
    c.insert({"a", "b", "c"});
}
