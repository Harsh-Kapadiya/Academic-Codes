#include <iostream>
using namespace std;
int main()
{
    int n = 10;
    int adj[10][10] = {0};
    int edges, vertex, i, j;
    cout << "Enter the number of edges: ";
    cin >> edges;

    for (i = 0; i < edges; i++)
    {
        cout << "Enter edge " << i + 1 << " (from to) using A-J: ";
        char u, v;
        cin >> u;
        cout << "enter edge connected to " << u << " : ";
        cin >> v;
        int from = u - 'A';
        int to   = v - 'A';

        adj[from][to] = 1;
    }

    cout << "\nAdjacency Matrix:\n    ";
    for (char c = 'A'; c <= 'J'; c++)
        cout << c << " ";
    cout << endl;

    for (int i = 0; i < n; i++)
    {
        cout << char('A' + i) << " : ";
        for (int j = 0; j < n; j++)
        {
            cout << adj[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}