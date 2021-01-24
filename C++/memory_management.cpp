#include <iostream>
using namespace std;

int main()
{
    // different styles of declaration and assignment using new
    int *p = new int;

    *p = 45;
    cout << "The value of p is : " << *p << endl;
    delete p;
    cout << "The value of p is : " << *p << endl;
    float *q = new float(9.8);
    int *arr = new int[8];

    // different styles of deleting allocated memory
    delete q;
    delete[] arr; // deleting the dynamically allocated array
    return 0;
}