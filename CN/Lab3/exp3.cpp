#include <iostream>
using namespace std;

int main()
{
    string data = "10011101 ";
    string gen = "1001";
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

    cout << "Transmitted Data: " << temp << endl;

    // Introduce error
    temp[2] = (temp[2] == '1') ? '0' : '1';

    bool error = false;
    for (int i = m; i < temp.length(); i++)
    {
        if (temp[i] == '1')
        {
            error = true;
            break;
        }
    }

    if (error)
        cout << "Error Detected" << endl;
    else
        cout << "No Error Detected" << endl;

    return 0;
}
