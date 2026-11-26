#include <iostream>
#include <vector>
using namespace std;
int main()
{
    int n = 6;
    vector<char> Routers = {'A', 'B', 'C', 'D', 'E', 'F'};
    vector<int> routing_Table_B = {5, 0, 8, 12, 6, 2};
    vector<int> routing_Table_D = {16, 12, 6, 0, 9, 10};
    vector<int> routing_Table_E = {7, 6, 3, 9, 0, 4};

    int Cost_CB = 2;
    int cost_CD = 3;
    int cost_CE = 5;

    vector<int> new_routing_table(n);
    vector <char> nextHop(n);

    for (int i = 0; i < n; i++)
    {
        int cost_via_B = routing_Table_B[i] + Cost_CB;
        int cost_via_D = routing_Table_D[i] + cost_CD;
        int cost_via_E = routing_Table_E[i] + cost_CE;

        int minCost = cost_via_E;
        char hop = 'E';
        if (minCost > cost_via_D)
        {
            minCost = cost_via_D;
            hop = 'D';
        }
        if (minCost > cost_via_B)
        {
            minCost = cost_via_B;
            hop = 'B';
        }
        new_routing_table[i] = minCost;
        nextHop[i] = hop;
    }


    new_routing_table[2] = 0; // Cost to reach itself is always 0
    nextHop[2] = '-'; // Next hop to reach itself is always itself
    cout << "Updated routing table for Router C:\n";
    cout << "Destination\tCost\tNext Hop\n";
    for (int i = 0; i < n; i++)
    {
        cout << Routers[i] << "\t\t" << new_routing_table[i] << "\t" << nextHop[i] << endl;
    }

    return 0;
}