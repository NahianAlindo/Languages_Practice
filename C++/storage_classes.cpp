// Storage Class	Keyword	      Lifetime	       Visibility	   Initial Value
// Automatic	     auto	    Function Block	     Local	        Garbage
// Register	        register	Function Block	     Local	        Garbage
// Mutable	        mutable	      Class	             Local	        Garbage
// External	         extern      Whole Program	     Global	          Zero
// Static	         static	     Whole Program	     Local	          Zero

#include <iostream>
using namespace std;

void func()
{
    static int i = 0;
    int j = 0;
    i++;
    j++;
    cout << "i=" << i << " and j=" << j << endl;
}

int main()
{
    register int counter = 0;
    //extern int count = 0; // he extern variable is visible to all the programs.
    //It is used if two or more files are sharing same variable or function.
    func();
    func();
    func();
}