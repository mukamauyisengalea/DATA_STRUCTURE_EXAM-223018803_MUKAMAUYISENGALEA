/*3.2 Function Example:
Let's write a function that adds two numbers and returns the result.*/
#include <iostream>
using namespace std;

// Function definition
int add(int a, int b) {
    return a + b;
}

int main() {
    int sum = add(5, 10);  // Calling the function
    cout << "The sum is: " << sum << endl;
    return 0;
}


