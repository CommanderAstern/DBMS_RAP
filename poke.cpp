// find the last digit of a number

#include <iostream>
using namespace std;

int main()
{
    int n, last_digit;
    cout << "Enter a number: ";
    cin >> n;
    last_digit = n % 10;
    cout << "The last digit of " << n << " is " << last_digit << endl;
    return 0;
}