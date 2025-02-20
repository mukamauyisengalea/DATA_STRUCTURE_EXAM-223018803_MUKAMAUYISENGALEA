/*3.	Build a Simple Calculator
Write a program with functions to perform basic arithmetic operations (addition, subtraction, multiplication, division).
 Ask the user which operation they want to perform and take two numbers as input.*/
#include <iostream>
using namespace std;

int addition(int num1, int num2) {
    return num1 + num2;
}

int substraction(int num1, int num2) {
    return num1 - num2;
}

int multiplication(int num1, int num2) {
    return num1 * num2;
}

double division(int num1, int num2) {
    if (num2 == 0) {
        cout << "Impossible to divide by zero" << endl;
        return 0;
    }
    return static_cast<double>(num1) / num2;
}

int main() {
    int a, b, choice;
    cout << "Enter two numbers: ";
    cin >> a >> b;

    cout << "CHOOSE OPERATION:\n"
         << "1. Addition\n"
         << "2. Subtraction\n"
         << "3. Multiplication\n"
         << "4. Division\n";
    cin >> choice;

    if (choice == 1) {
        cout << "Result: " << addition(a, b) << endl;
    } else if (choice == 2) {
        cout << "Result: " << substraction(a, b) << endl;
    } else if (choice == 3) {
        cout << "Result: " << multiplication(a, b) << endl;
    } else if (choice == 4) {
        cout << "Result: " << division(a, b) << endl;
    } else {
        cout << "Invalid choice" << endl;
    }
    return 0;
}

