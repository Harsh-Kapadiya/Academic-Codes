#include <iostream>
using namespace std;

string Stuffed_Bit(string data)
{
    string stuffed = "";
    int count = 0;
    for (char bit : data)
    {
        stuffed += bit;
        if (bit == '1')
        {
            count++;
            if (count == 5)
            {
                stuffed += '0';
                count = 0;
            }
        }
        else
        {
            count = 0;
        }
    }
    return stuffed;
}
int main()
{
    string data;
    cout << "Enter the binary data: ";
    cin >> data;

    string Frame = Stuffed_Bit(data);
    cout << "Stuffed data: " << Frame << endl;
    return 0;
}