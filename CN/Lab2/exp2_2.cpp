#include <iostream>
#include <climits>
using namespace std;

int main() {
    int V, E;
    cout << "Enter number of vertices: ";
    cin >> V;

    cout << "Enter number of edges: ";
    cin >> E;

    int graph[V][V];

    // Initialize matrix with 0
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            graph[i][j] = 0;
        }
    }

    cout << "\nEnter edges (source destination weight)\n";
    cout << "Example: a b 4\n\n";

    for (int i = 0; i < E; i++) {
        char srcChar, destChar;
        int weight;

        cin >> srcChar >> destChar >> weight;

        int src = srcChar - 'a';
        int dest = destChar - 'a';

        // Undirected graph
        graph[src][dest] = weight;
        graph[dest][src] = weight;
    }

    // ---- Prim's Algorithm ----
    int key[V], parent[V];
    bool mstSet[V];

    for (int i = 0; i < V; i++) {
        key[i] = INT_MAX;
        mstSet[i] = false;
    }

    // Start MST from node 'a' (can be changed)
    key[0] = 0;
    parent[0] = -1;

    for (int count = 0; count < V - 1; count++) {
        int min = INT_MAX, u = -1;

        for (int v = 0; v < V; v++) {
            if (!mstSet[v] && key[v] < min) {
                min = key[v];
                u = v;
            }
        }

        mstSet[u] = true;

        for (int v = 0; v < V; v++) {
            if (graph[u][v] != 0 &&
                !mstSet[v] &&
                graph[u][v] < key[v]) {

                parent[v] = u;
                key[v] = graph[u][v];
            }
        }
    }

    cout << "\nEdges in Minimum Spanning Tree (Prim's Algorithm):\n";
    for (int i = 1; i < V; i++) {
        cout << char('a' + parent[i]) << " - "
             << char('a' + i)
             << " : " << graph[i][parent[i]] << endl;
    }

    return 0;
}
