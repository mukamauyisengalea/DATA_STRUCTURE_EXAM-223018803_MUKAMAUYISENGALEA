/*3.3 Function with void Return Type
Some functions don't return anything but still perform a task. These are called void functions.
Example:*/
#include <iostream>
#include <string>

using namespace std;

void greet(string name) {
    cout << "Hello, " << name << "!" << endl;
}

int main() {
    greet("Alice");  // Calling the function
    return 0;
}


