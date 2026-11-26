// single source shortest path using dkjistra algorithm
#include <stdio.h>
#define INF 99999
struct Edge
{
    int src, dest, weight;
};
int main()
{
    int V, E;
    printf("Enter number of vertices: ");
    scanf("%d", &V);
    printf("Enter number of edges: ");
    scanf("%d", &E);
    struct Edge edge[E];
    printf("\nEnter edges (source destination weight):\n");
    for (int i = 0; i < E; i++)
    {
        scanf("%d %d %d", &edge[i].src, &edge[i].dest, &edge[i].weight);
    }
    int source;
    printf("\nEnter source vertex: ");
    scanf("%d", &source);
    int dist[V];
    for (int i = 0; i < V; i++)
        dist[i] = INF;
    dist[source] = 0;

    for (int i = 1; i <= V - 1; i++)
    {
        for (int j = 0; j < E; j++)
        {
            int u = edge[j].src;
            int v = edge[j].dest;
            int w = edge[j].weight;

            if (dist[u] != INF && dist[u] + w < dist[v])
            {
                dist[v] = dist[u] + w;
            }
        }
    }
    printf("\nVertex\tDistance from Source\n");
    for (int i = 1; i <= V; i++)
    {
        printf("%d\t%d\n", i, dist[i]);
    }
    return 0;
}