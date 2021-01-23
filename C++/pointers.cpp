#include <iostream>
using namespace std;

int main()
{
    int number = 30;
    int *p;
    p = &number;
    cout << "Address of number variable: " << &number << endl;
    cout << "Address of p " << p << endl;
    cout << "Address of p+1 " << p + 1 << endl;
    cout << "Value of p " << *p << endl;

    // array of pointers
    int ptr1[5];
    int *ptr2[5];

    int i;
    cout << "Enter 5 numbers:" << endl;
    for (i = 0; i < 5; i++)
    {
        cin >> ptr1[i];
    }

    for (i = 0; i < 5; i++)
    {
        ptr2[i] = &ptr1[i];
    }

    cout << "the pointer array values are: " << endl;

    for (i = 0; i < 5; i++)
    {
        cout << *ptr2[i] << endl;
    }

    // array of pointers to strings
    char *names[] = {
        "John", "Peter", "Marco", "Devin", "Ronan"};

    for (i = 0; i < 5; i++)
    {
        cout << names[i] << endl;
    }
    return 0;
}