#include <iostream>
#include <climits>
using namespace std;

int main()
{
    int V, E;

    cout << "Enter number of vertices: ";
    cin >> V;

    cout << "Enter number of edges: ";
    cin >> E;

    int graph[V][V];

    // Initialize adjacency matrix with 0
    for (int i = 0; i < V; i++)
    {
        for (int j = 0; j < V; j++)
        {
            graph[i][j] = 0;
        }
    }

    cout << "\nEnter edges (source destination weight)\n";
    cout << "Example: a b 4\n\n";

    for (int i = 0; i < E; i++)
    {
        char srcChar, destChar;
        int weight;

        cin >> srcChar >> destChar >> weight;

        int src = srcChar - 'a';
        int dest = destChar - 'a';

        // Undirected graph
        graph[src][dest] = weight;
        graph[dest][src] = weight;
    }

    // ---- Dijkstra’s Algorithm ----
    int dist[V];
    bool visited[V];

    for (int i = 0; i < V; i++)
    {
        dist[i] = INT_MAX;
        visited[i] = false;
    }

    // Source node fixed as 'a'
    int source = 0;
    dist[source] = 0;

    for (int count = 0; count < V - 1; count++)
    {
        int minDist = INT_MAX, u = -1;

        // Pick vertex with minimum distance
        for (int i = 0; i < V; i++)
        {
            if (!visited[i] && dist[i] < minDist)
            {
                minDist = dist[i];
                u = i;
            }
        }

        visited[u] = true;

        // Update distances of adjacent vertices
        for (int v = 0; v < V; v++)
        {
            if (!visited[v] && graph[u][v] != 0 &&
                dist[u] != INT_MAX &&
                dist[u] + graph[u][v] < dist[v])
            {

                dist[v] = dist[u] + graph[u][v];
            }
        }
    }

    // Output result
    cout << "\nShortest path distances from source 'a':\n";
    for (int i = 0; i < V; i++)
    {
        cout << "a -> " << char('a' + i) << " = ";
        if (dist[i] == INT_MAX)
            cout << "INF";
        else
            cout << dist[i];
        cout << endl;
    }

    return 0;
}
