// count to infinity problem in dvr

#include <iostream>
using namespace std;

int main()
{
    int cost = 1; // cost between B and C
    int INF = 16; // infinity (as in RIP)

    // Initial values
    int BtoD = 2; // B -> C -> D
    int CtoD = 1; // direct

    cout << "Initial State:\n";
    cout << "B -> D = " << BtoD << endl;
    cout << "C -> D = " << CtoD << endl;

    // Link failure
    cout << "\nLink C-D crashes\n";
    CtoD = INF;

    // Step (i)
    CtoD = cost + BtoD; // C uses B
    cout << "\nStep (i):\n";
    cout << "C -> D = " << CtoD << endl;

    // Step (ii)
    BtoD = cost + CtoD; // B uses C
    cout << "\nStep (ii):\n";
    cout << "B -> D = " << BtoD << endl;

    // Step (iii)
    CtoD = cost + BtoD;
    cout << "\nStep (iii):\n";
    cout << "C -> D = " << CtoD << endl;

    // Step (iv)
    BtoD = cost + CtoD;
    cout << "\nStep (iv):\n";
    cout << "B -> D = " << BtoD << endl;

    return 0;
}