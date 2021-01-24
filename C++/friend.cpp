#include <iostream>
using namespace std;
class B; // forward declarartion. it is a must for friend to work
// and always use setters and getters
class A
{
    int x;

public:
    void setdata(int i)
    {
        x = i;
    }
    friend void min(A, B); // friend function.
    friend class B;
};
class B
{
    int y;

public:
    void setdata(int i)
    {
        y = i;
    }
    friend void min(A, B); // friend function
    void display(A &a)
    {
        cout << "value of x is : " << a.x;
    }
};
void min(A a, B b)
{
    if (a.x <= b.y)
        std::cout << a.x << std::endl;
    else
        std::cout << b.y << std::endl;
}
int main()
{
    A a;
    B b;
    a.setdata(10);
    b.setdata(20);
    min(a, b);
    b.display(a);
    return 0;
}