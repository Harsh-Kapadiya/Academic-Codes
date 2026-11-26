#include <iostream>
using namespace std;

string Byte_stuffing(string data)
{
    char stx = 'S';
    char dle = 'D';
    char etx = 'E';
    string frame;

    frame += dle;
    frame += stx;

    for (char ch : data)
    {
        if (ch == dle)
        {
            frame += dle;
        }
        frame += ch;
    }
    frame += dle;
    frame += etx;

    return frame;
}
int main()
{
    string data;
    cout << "Enter the data: ";
    cin >> data;

    string frame = Byte_stuffing(data);
    cout << "Stuffed data is: "<< frame << endl;
    return 0;
}