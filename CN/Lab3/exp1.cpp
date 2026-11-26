#include <iostream>
#include <bitset>
using namespace std;
int main()
{
    int first_d, sec_d;

    cout << "Enter the first coding schema: ";
    cin >> first_d;

    cout << "Enter the second coding schema: ";
    cin >> sec_d;

    cout << "Result: " << (first_d ^ sec_d) << endl;

    string result = to_string(first_d ^ sec_d);
     
    int hamming_distance = bitset<32>(result).count();

    cout << "Hamming Distance (Shortest distance) is: " << hamming_distance << endl;


    return 0;
}