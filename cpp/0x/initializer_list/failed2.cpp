#include <initializer_list>
#include <string>

template <typename T>
struct thing
{
    void insert(T const&) {}
    void insert(T&&) {}
    void insert(std::initializer_list<T>) {}
};

int main() 
{
    thing<std::string> x;
    x.insert("a");
    x.insert({"a"});
    x.insert({"a", "b"});
}
