#include <stdio.h>
#define MAX 100

void transitive_closure(int graph[MAX][MAX], int closure[MAX][MAX], int n)
{
    // Initialize closure matrix with graph values
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            closure[i][j] = graph[i][j];
        }
        closure[i][i] = 1; // Each node is reachable from itself
    }

    // Floyd-Warshall Algorithm
    for (int k = 0; k < n; k++)
    {
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                closure[i][j] = closure[i][j] ||
                                (closure[i][k] && closure[k][j]);
            }
        }
    }

    // Print result
    printf("Transitive Closure:\n");
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("%d ", closure[i][j]);
        }
        printf("\n");
    }
}

int main()
{
    int graph[MAX][MAX];
    int closure[MAX][MAX];
    int n;
    printf("Enter the size of the square matrix: ");
    scanf("%d",&n);

    printf("Enter the adjacency matrix (%dx%d):\n", n,n);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            scanf("%d", &graph[i][j]);
        }
    }

    transitive_closure(graph, closure, n);

    return 0;
}