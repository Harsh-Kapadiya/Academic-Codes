#include <iostream>
using namespace std;

int main()
{
    string data = "10100001"; // x⁷ + x⁵ + 1
    string gen = "1001";      // x³ + 1
    int m = data.length();
    int g = gen.length();

    // Append zeros
    for (int i = 0; i < g - 1; i++)
        data += '0';

    string temp = data;

    for (int i = 0; i < m; i++)
    {
        if (temp[i] == '1')
        {
            for (int j = 0; j < g; j++)
            {
                temp[i + j] = (temp[i + j] == gen[j]) ? '0' : '1';
            }
        }
    }

    cout << "CRC Remainder: ";
    for (int i = m; i < temp.length(); i++)
        cout << temp[i];

    return 0;
}
