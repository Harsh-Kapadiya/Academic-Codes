#include <iostream>
#include <algorithm>
using namespace std;

struct Edge
{
    int src, dest, weight;
};

int parent[100];

int find(int i)
{
    if (parent[i] == i)
        return i;
    return find(parent[i]);
}

void unionSet(int u, int v)
{
    parent[u] = v;
}

int main()
{
    int V, E;
    cout << "Enter number of vertices and edges: ";
    cin >> V >> E;

    Edge edges[E];

    cout << "Enter edges \n (src dest weight)\n";
    for (int i = 0; i < E; i++)
    {
        cin >> edges[i].src >> edges[i].dest >> edges[i].weight;
    }

    // Initialize parent
    for (int i = 0; i < V; i++)
        parent[i] = i;

    // Sort edges by weight
    sort(edges, edges + E, [](Edge a, Edge b)
         { return a.weight < b.weight; });

    cout << "\nEdges in MST (Kruskal):\n";
    int count = 0, i = 0;

    while (count < V - 1)
    {
        int u = find(edges[i].src);
        int v = find(edges[i].dest);

        if (u != v)
        {
            cout << edges[i].src << " - " << edges[i].dest
                 << " : " << edges[i].weight << endl;
            unionSet(u, v);
            count++;
        }
        i++;
    }

    return 0;
}
