#include <iostream>
using namespace std;

class Base
{
    int a;
    char c;
};

int main()
{
    Base b;
    //sizeof is a compile time operator
    cout << "Size of int: " << sizeof(int) << " bytes" << endl;
    cout << "Size of char: " << sizeof(char) << " bytes" << endl;
    cout << "Size of b: " << sizeof(b) << " Bytes" << endl;

    int *ptr1 = new int(10);
    cout << "size of ptr1 is: " << sizeof(ptr1) << endl;
    cout << "size of ptr1's value is: " << sizeof(*ptr1) << endl;
}