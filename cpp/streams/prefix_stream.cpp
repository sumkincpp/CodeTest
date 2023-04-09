#include <iostream>
#include <cstring>
#include <functional> // std::function
#include <chrono> // std::time_t, ..

std::string current_time(const std::string& format_str)
{
    // "%Y-%m-%d %H:%M:%S"
    std::time_t now = std::time(nullptr);
    
    // Convert to a local time struct
    std::tm* now_tm = std::localtime(&now);

    std::string result(80, '\0');

    // Format the time as a string
    char buf[80] = {};
    std::strftime(buf, sizeof(buf), format_str.c_str(), now_tm);
    
    return buf;
}

class PrefixedStream {
public:
    explicit PrefixedStream(std::ostream& stream, std::function<std::string()> prefix_fn)
        : _stream(stream), _prefix_fn(prefix_fn), _eol_seen(true) {}

    template<typename T>
    PrefixedStream& operator<<(const T& value) {
        if (_eol_seen) {
            _stream << _prefix_fn();
            _eol_seen = false;
        }
        _stream << value;
        return *this;
    }

    PrefixedStream& operator<<(std::ostream& (*manip)(std::ostream&)) {
        _stream << manip;

        // hello, yeees it is
        if (manip == static_cast<std::ostream& (*)(std::ostream&)>(std::endl)) {
            _eol_seen = true;
        }

        return *this;
    }

private:
    std::ostream& _stream;
    std::function<std::string()> _prefix_fn;
    bool _eol_seen;
};


int main(int argc, char *argv[])
{
    auto prefix_fn = []() { return current_time("%Y-%m-%d %H:%M:%S") + " "; };
    PrefixedStream stream(std::cout, prefix_fn);

    stream << "hello" << "\n" << "world" << 1 << std::endl;
    stream << "hello" << "world" << 2 << std::endl;

    // 2023-04-08 19:13:17 hello
    // world1
    // 2023-04-08 19:13:17 helloworld2
}
