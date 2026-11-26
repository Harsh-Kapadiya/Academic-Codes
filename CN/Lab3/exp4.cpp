#include <iostream>
using namespace std;

int main()
{
    int data[8] = {1, 0, 1, 0, 1, 1, 1, 1};
    int hamming[12];

    int j = 0;
    for (int i = 1; i <= 12; i++)
    {
        if (i == 1 || i == 2 || i == 4 || i == 8)
            hamming[i - 1] = 0;
        else
            hamming[i - 1] = data[j++];
    }

    hamming[0] = hamming[2] ^ hamming[4] ^ hamming[6] ^ hamming[8] ^ hamming[10];
    hamming[1] = hamming[2] ^ hamming[5] ^ hamming[6] ^ hamming[9] ^ hamming[10];
    hamming[3] = hamming[4] ^ hamming[5] ^ hamming[6] ^ hamming[11];
    hamming[7] = hamming[8] ^ hamming[9] ^ hamming[10] ^ hamming[11];

    cout << "Hamming Code: ";
    for (int i = 0; i < 12; i++)
        cout << hamming[i];

    return 0;
}
 