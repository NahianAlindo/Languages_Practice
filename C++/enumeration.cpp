// enum improves type safety
// enum can be easily used in switch
// enum can be traversed
// enum can have fields, constructors and methods
// enum may implement many interfaces but cannot extend any class
// because it internally extends Enum class

#include <iostream>
using namespace std;
enum week
{
    Saturday,
    Sunday,
    Monday,
    Tuesday,
    Wednesday,
    Thursday,
    Friday
};
int main()
{
    week day;
    day = Monday;
    cout << "Day " << day + 1 << endl;
    return 0;
}