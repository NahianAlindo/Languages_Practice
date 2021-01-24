#include <iostream>
using namespace std;

void swap(int &p, int &q)
{
    int temp;
    temp = p;
    p = q;
    q = temp;
}

struct profile
{
    int id;
};

struct employee
{
    profile p;
};

int main()
{
    int a = 10;
    int &value = a; // reference declaration
    // references can be used as aliases to other variables
    // IMPORTANT: initialize references at declaration, otherwise error
    // IMPORTANT: references cannot be modified. compile error
    // reference to another reference is not possible
    // there is nothing called reference arithmetic like pointer arithmetic
    cout << value << endl;
    int b = 10;
    int c = 20;
    swap(b, c); // look at the function declaration
    cout << b << " " << c << endl;

    // references can be used as shortcuts too
    employee e;
    int &ref = e.p.id; // shortcut declaration using references
    ref = 34;
    cout << ref << endl;
    return 0;
}