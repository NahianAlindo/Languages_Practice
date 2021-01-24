#include <iostream>
using namespace std;

class Employee
{
public: // public declaration
    // data members and instance variables
    int id;
    string name;
    float salary;

    // default constructor
    Employee()
    {
        cout << "Default constructor invoked" << endl;
    }

    ~Employee()
    {
        cout << "Destructor invoked" << endl;
    }

    // parameterized constructor
    Employee(int id, string name, float salary)
    {
        this->id = id;
        this->name = name;
        this->salary = salary;
    }

    void insert(int i, string n, float s) // mutator or, setter method
    {
        id = i;
        name = n;
        salary = s;
    }

    void display() // accessor or, getter method
    {
        cout << id << " " << name << " " << salary << endl;
    }
};

int main()
{
    Employee e;
    e.insert(1093, "Nahian Rifaat", 10000);
    e.display();
    Employee e1;
    Employee e2(1093, "Nazib Riasat", 10000);
    e2.display();
    return 0;
}