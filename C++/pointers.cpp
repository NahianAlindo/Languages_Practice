#include <iostream>
using namespace std;

int add(int a, int b)
{
    return a + b;
}

void printName(char *name)
{
    cout << "my name is: " << name << endl;
}

void func1()
{
    cout << "Hi from func1" << endl;
}

void func2(void(*funcptr))
{
    funcptr();
}

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

    // void pointers

    void *ptr;
    int a = 9;
    ptr = &a;
    cout << "The address of a is " << &a << endl;
    cout << "The value of ptr is " << ptr << endl;

    void *ptr3;
    int *ptr4;
    int data = 10;
    ptr3 = &data;
    ptr4 = (int *)ptr3; // type casting necessary to use void pointer
    // to store in integer pointer
    cout << "The value in ptr3 is: " << *ptr4 << endl;

    // pointer to pointer
    int *e;
    int d = 8;
    int **f;
    e = &d;
    f = &e;
    cout << "The value of *f is: " << *f << endl;
    cout << "The value of *(*f) is: " << *(*f) << endl;

    // function pointers
    cout << "The address to the main function is: " << &main << endl;
    int (*funcPtr)(int, int); // function pointer declaration
    funcPtr = add;            // function pointer assignment
    int sum = funcPtr(a, d);  // function pointer usage
    cout << "Function Pointer returned: " << sum << endl;

    char s[20];
    void (*Ptr)(char *);
    Ptr = printName;
    cout << "Enter the name of the person: " << std::endl;
    cin >> s;
    cout << s << endl;
    Ptr(s);

    // passing a function pointer as a parameter
    // func2(func1);// auto indent is interrupting
    return 0;
}