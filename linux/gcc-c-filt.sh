echo "void f1(int , int) {} " | g++ -x c++ -S - -o- | grep "^_.*:$" | sed -e 's/:$//' | c++filt
