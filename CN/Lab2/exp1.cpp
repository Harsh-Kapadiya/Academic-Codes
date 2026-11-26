#include <iostream>
using namespace std;

int main() {
    int n, e;

    cout << "Enter number of nodes: ";
    cin >> n;

    // Adjacency matrix
    int matrix[n][n];

    // Initialize matrix with 0
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            matrix[i][j] = 0;
        }
    }

    cout << "Enter number of edges: ";
    cin >> e;

    int src, dest, weight;

    cout << "Enter edges in format:\nSource Destination Weight\n";
    for (int i = 1; i <= e; i++) {
        cin >> src >> dest >> weight;

        // Adjust index (nodes start from 1)
        matrix[src][dest] = weight;
    }

    // Display adjacency matrix
    cout << "\nAdjacency Matrix:\n\n";
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << matrix[i][j] << "\t";
        }
        cout << endl;
    }

    return 0;
}
