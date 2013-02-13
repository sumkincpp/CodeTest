#include <fstream>
#include <iostream>

using std::cout;

int main ()
{
    char ar[100]; // буфер, в который будем считывать текст
    int num = 0

    std::ifstream fin("data.txt"); //открываем файл
    fin >> ar >> num; // аналогично cin, считывание до пробела

    cout << ar << " " << num; // печатаем в консоль

    fin.close(); // закрываем файл

    return 0;
}
