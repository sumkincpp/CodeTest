#include <fstream>
#include <iostream>

using std::cout;

int main ()
{
    char ar[100]; // �����, � ������� ����� ��������� �����
    int num = 0

    std::ifstream fin("data.txt"); //��������� ����
    fin >> ar >> num; // ���������� cin, ���������� �� �������

    cout << ar << " " << num; // �������� � �������

    fin.close(); // ��������� ����

    return 0;
}
