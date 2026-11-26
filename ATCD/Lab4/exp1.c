#include <stdio.h>
int main()
{
    int n, m, i, j;
    int start;
    printf("Enter number of states: ");
    scanf("%d", &n);
    printf("Enter number of input symbols: ");
    scanf("%d", &m);
    char symbols[m];
    int dfa[n][m];
    int final[n];
    printf("Enter input symbols:\n");
    for (i = 0; i < m; i++) 
        scanf(" %c", &symbols[i]);
    printf("Enter DFA transition table:\n");
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
        {
            scanf("%d", &dfa[i][j]);
        }
    }
    printf("Enter start state: ");
    scanf("%d", &start);
    printf("Enter final states (1 if final, 0 otherwise):\n");
    for (i = 0; i < n; i++)
        scanf("%d", &final[i]);
    printf("\nRegular Grammar Productions:\n");
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < m; j++)
        {
            printf("Q%d -> %c Q%d", i, symbols[j], dfa[i][j]);
            if (final[dfa[i][j]])
                printf(" | %c", symbols[j]);
            printf("\n");
        }
    }
    printf("\nStart Symbol: Q%d\n", start);
    return 0;
}