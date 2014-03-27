#include <iostream>

namespace quoting {
  struct quoting_proxy {
      explicit quoting_proxy(std::ostream & os):os(os){}

      template<typename Rhs>
      friend std::ostream & operator<<(quoting_proxy const& q,
                                       Rhs const& rhs) {
          return q.os << rhs;
      }

      friend std::ostream & operator<<(quoting_proxy const& q,
                                       std::string const& rhs) {
          return q.os << "'" << rhs << "'";
      }

      friend std::ostream & operator<<(quoting_proxy const& q,
                                       char const* rhs) {
          return q.os << "'" << rhs << "'";
      }
  private:
      std::ostream & os;
  };

  struct quoting_creator { } quote;
  quoting_proxy operator<<(std::ostream & os, quoting_creator) {
      return quoting_proxy(os);
  }
}

int main() {
    std::cout << quoting::quote << "hello" << std::endl;
}
