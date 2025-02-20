/*1.	Create a Program to Check Even or Odd
Write a program that asks the user to enter a number and checks whether the number is even or odd using an if-else statement.
*/
#include<iostream>
Using namespace std;
int main(){
int num;
cout<<"Enter a number:";
cin>>num;
if((num%2)==0){
cout<<"Number is even";}
else{
cout<<"number is odd";
}
return 0;
}
