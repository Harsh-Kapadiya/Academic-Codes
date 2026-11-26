#include <iostream>
#include <limits.h>
using namespace std;

#define V 8 // Nodes: X Y Z V W U T S

int minDistance(int dist[], bool visited[])
{
    int min = INT_MAX, min_index;

    for (int v = 0; v < V; v++)
    {
        if (visited[v] == false && dist[v] <= min)
        {
            min = dist[v];
            min_index = v;
        }
    }

    return min_index;
}

void dijkstra(int graph[V][V], int src)
{
    int dist[V];
    bool visited[V];

    for (int i = 0; i < V; i++)
    {
        dist[i] = INT_MAX;
        visited[i] = false;
    }

    dist[src] = 0;

    for (int count = 0; count < V - 1; count++)
    {
        int u = minDistance(dist, visited);
        visited[u] = true;

        for (int v = 0; v < V; v++)
        {
            if (!visited[v] && graph[u][v] &&
                dist[u] != INT_MAX &&
                dist[u] + graph[u][v] < dist[v])
            {
                dist[v] = dist[u] + graph[u][v];
            }
        }
    }

    char nodes[V] = {'X', 'Y', 'Z', 'V', 'W', 'U', 'T', 'S'};

    cout << "Shortest distance from node X\n";
    cout << "Node\tCost\n";

    for (int i = 0; i < V; i++)
        cout << nodes[i] << "\t" << dist[i] << endl;
}

int main()
{
    int graph[V][V] =
        {
            /*X*/ {0, 6, 0, 3, 1, 0, 0, 0},
            /*Y*/ {6, 0, 14, 1, 0, 0, 4, 0},
            /*Z*/ {0, 14, 0, 0, 0, 0, 2, 0},
            /*V*/ {3, 1, 0, 0, 1, 1, 9, 0},
            /*W*/ {1, 0, 0, 1, 0, 3, 0, 0},
            /*U*/ {0, 0, 0, 1, 3, 0, 2, 4},
            /*T*/ {0, 4, 2, 9, 0, 2, 0, 1},
            /*S*/ {0, 0, 0, 0, 0, 4, 1, 0}};

    dijkstra(graph, 0); // 0 = X

    return 0;
}