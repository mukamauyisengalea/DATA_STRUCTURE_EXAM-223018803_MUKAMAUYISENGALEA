/*2.	Loop through an Array
Create an array of 5 integers. Use a for loop to print all the numbers.*/
#include <iostream>
using namespace std;

int main() {
    int num, array[5] = {1, 2, 3, 4, 5};
    
    for (num = 0; num < 5; num++) {
        cout << array[num] << endl;
    }
    
    return 0;
}


