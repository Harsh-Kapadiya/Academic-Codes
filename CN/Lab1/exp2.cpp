#include <iostream>
using namespace std;

int main() {
    int n = 10;                 // Number of nodes (A–J)
    int adj[10][10] = {0};      // Adjacency matrix initialized to 0
    int edges;

    cout << "Enter number of edges: ";
    cin >> edges;

    cout << "Enter edges (from to) using A-J:\n";
    for(int i = 0; i < edges; i++) {
        char u, v;
        cin >> u >> v;

        int from = u - 'A';     // Convert char to index
        int to   = v - 'A';

        adj[from][to] = 1;      // Directed edge
    }

    cout << "\nAdjacency Matrix:\n    ";
    for(char c = 'A'; c <= 'J'; c++)
        cout << c << " ";
    cout << endl;

    for(int i = 0; i < n; i++) {
        cout << char('A' + i) << " : ";
        for(int j = 0; j < n; j++) {
            cout << adj[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
